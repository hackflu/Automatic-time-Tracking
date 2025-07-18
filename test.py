# try:
#     lists = [1,1,2]
#     print(lists[len(lists)-2])
# except IndexError:
#     pass

# print(len(lists))
# x = list(lists)
# print(x[0])

# from datetime import date
# d0 = date(2022, 8, 18)
# d1 = date(2022, 10, 26)
# delta = d1 - d0
# print(delta.days)

# import time
# start = time.time()
# for _ in range(10):
#     print('a')
# end = time.time()
# print(start - end)
# from time import strftime
#
# # print(strftime('%H:%M:%S'))
# x = strftime('%H')
# y = strftime('%M')
# z = strftime('%S')
# l = []
# o = [int(x),int(y),int(z)]
# l.extend(o)
# print(l)
# input('enter:')
# s = strftime('%H')
# k = strftime('%M')
# n = strftime('%S')
# m = []
# j = [int(s ), int(k) ,int(n)]
# m.extend(j)
# for x in range(len(m)):
#     if m[x] > l[x]:
#         print(m)
#         print(m[x] - l[x])
#     else:
#         pass
#
# from datetime import datetime
# now = datetime.now()
# input("enter: ")
# later = datetime.now()
# difference = (later - now).total_seconds()
# print(difference)

# x = {'about yourself' : [{'name' : 'satyam','Roll': 35}]}
#
# x['about yourself'].append({'name' : 'rishab','roll': 43})
# print(x['about yourself'])
# from win32gui import GetForegroundWindow
# import psutil
# import time
# import win32process
#
# process_time={}
# timestamp = {}
# while True:
#     current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
#     timestamp[current_app] = int(time.time())
#     time.sleep(1)
#     if current_app not in process_time.keys():
#         process_time[current_app] = 0
#     process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
#     print(process_time.values())

from datetime import datetime,timedelta

start = datetime.now()
input('g')
end = datetime.now()

differ = end - start
x = []
x.append(differ)
print(x)