from datetime import datetime, timedelta
import sys
import time
from time_record import TimeEntry, Activity, AcitivyList
import json

if sys.platform in ["Windows", "win32", "cygwin"]:
    import win32gui
    import uiautomation as auto

active_window = ""
previous_windows = ['']
start_time = datetime.now()
activeList = AcitivyList([])


def get_current_windowTitle():  ## capture the current window tab
    global active_window
    if sys.platform in ["Windows", "win32", "cygwin"]:
        w = win32gui
        capture = w.GetForegroundWindow()
        active_window = w.GetWindowText(capture)

    else:
        print(f"sys.platform={sys.platform} is not supported")

    return active_window


def url_sorting(url):  ## sorting the current tab url
    string_list = url.split('/')
    return string_list[2]


def get_chrome_url():  ## captureing the link of the current tab of chrome

    if sys.platform in ["Windows", "win32", "cygwin"]:
        # try:
        chrome_window = auto.GetForegroundWindow()
        control_chrome = auto.ControlFromHandle(chrome_window)
        edit = control_chrome.EditControl()

        current_link = f'https://{edit.GetValuePattern().Value}'
        return current_link
        # except AttributeError:
        #     pass
    else:
        print(f"sys.platform : {sys.platform} not supported")


if __name__ == '__main__':
    filter_out = []
    first_time = True
    current = ""
    try:
        while True:
            new_window = get_current_windowTitle()
            previous_windows.append(new_window)
            # print(previous_windows)
            if new_window != current:
                if new_window not in previous_windows[len(previous_windows) - 2]:
                    # with open('activity.json' , 'w') as data

                    if "Google Chrome" in new_window:
                        if "New Tab - Google Chrome" in new_window:
                            current = "Chrome Tab"
                            filter_out.append(current)
                            print(current)


                        elif "GitHub -" in new_window:
                            current = "Github"
                            filter_out.append(current)
                            print(current)


                        elif "Stack Overflow" in new_window:
                            current = 'Stack Overflow'
                            filter_out.append(current)
                            print(current)


                        elif "Instagram" in new_window:
                            current = 'Instagram'
                            filter_out.append(current)
                            print(current)

                        else:
                            try:
                                url_window = get_chrome_url()
                                if url_window.endswith("://"):
                                    current = new_window
                                    filter_out.append(current)
                                    print(current)

                                else:
                                    current = url_sorting(url_window)
                                    filter_out.append(current)
                                    print(current)

                                    # pass

                            except AttributeError:
                                pass
                    elif ".py" in new_window:
                        current = 'Code'
                        filter_out.append(current)
                        print(current)

                    elif "Microsoft​ Edge" in new_window:
                        if "New tab -" or 'New tab and' in new_window:
                            current = "Edge Tab"
                            filter_out.append(current)
                            print(current)

                    else:
                        current = new_window
                        filter_out.append(current)
                        print(current)
                    #
                    if not first_time:
                        end_time = datetime.now()
                        capture_time = TimeEntry(start_time, end_time)
                        serialize_time = capture_time.serialize()
                        # print(serialize_time)

                        ## check whether the same activitie exist or not
                        exists = False

                        for activityies in activeList.activities:
                            if activityies.name == filter_out[len(filter_out) - 2]:
                                exists = True
                                activityies.time_entries.append(capture_time)
                        if not exists:
                            activity = Activity(filter_out[len(filter_out)-2], [capture_time])
                            activeList.activities.append(activity)
                        with open('activities.json', 'w') as json_file:
                            json.dump(activeList.serialize(), json_file,
                                      indent=4, sort_keys=True)
                            start_time = datetime.now()

                    first_time = False
                    # current = new_window

            time.sleep(1)
    except KeyboardInterrupt:
        with open('activities.json', 'w') as json_file:
            json.dump(activeList.serialize(), json_file, indent=4, sort_keys=True)