# git create repo pages
# curl -u 'stella-vir' https://api.github.com/user/repos -d '{"name":"timeManagement"}'
# password: Personal access tokens
# repo url: https://github.com/stella-vir/timeManagement

weeks = [0, 1],
week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
start_time = ['4:45', '9:00', '12:30'],
end_time = ['13:15', '16:30', '20:00']

class Calender:

    def __init__(self):
        self.schedules = []
        # self.schedules = {
        #     weeks: weeks,
        #     week_days: week_days,
        #     start_time: start_time,
        #     end_time: end_time
        # }

    def add(self, schedule):
        self.schedules.append(schedule)

    def size(self):
        return len(self.schedules)

    def get_schedules(self):
        return self.schedules

    def get_gross_income(self):
        pass
