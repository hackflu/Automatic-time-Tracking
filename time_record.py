

class AcitivyList:
    def __init__(self, activities):
        self.activities = activities

    def serialize(self):
        return {
            'activities': self.activities_to_json()
        }

    def activities_to_json(self):
        activities_ = []
        for activity in self.activities:
            activities_.append(activity.serialize())

        return activities_
class Activity:
    def __init__(self, name, time_entries):
        self.name = name
        self.time_entries = time_entries

    def serialize(self):
        return {
            'name': self.name,
            'time_entries': self.entire_to_json()
        }

    def entire_to_json(self):
        time_list = []
        for time in self.time_entries:
            time_list.append(time.serialize())
        return time_list

class TimeEntry():

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


    def total_time(self):
        time_in_seconds = self.end_time - self.start_time
        return time_in_seconds

    def serialize(self):
        return {

            'start_time': self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'days' : self.end_time.strftime("%Y-%m-%d"),
            'hour' : int(self.start_time.strftime("%H")) - int(self.end_time.strftime('%H')),
            'minutes' : int(self.start_time.strftime('%M')) - int(self.end_time.strftime("%M")),
            'seconds' : self.total_time().total_seconds(),
            'end_time': self.end_time.strftime("%Y-%m-%d %H:%M:%S")

        }


