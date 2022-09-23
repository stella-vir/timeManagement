# git create repo pages
# curl -u 'stella-vir' https://api.github.com/user/repos -d '{"name":"timeManagement"}'
# password: Personal access tokens
# repo url: https://github.com/stella-vir/timeManagement

weeks = [0, 1],
week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
start_time = ['4:45', '9:00', '12:30'],
end_time = ['13:15', '16:30', '20:00']

class Calender:

    def __init__(self, max_size):
        self.schedules = []
        self.max_size = max_size
        # self.schedules = {
        #     weeks: weeks,
        #     week_days: week_days,
        #     start_time: start_time,
        #     end_time: end_time
        # }

    def add(self, schedule):
        if self.size() == self.max_size:
            raise OverflowError('Reached max size')
        self.schedules.append(schedule)

    def size(self):
        return len(self.schedules)

    def get_schedules(self):
        return self.schedules

    def get_timing(self, timing_map):
        timing = []
        for s in self.schedules:
            # dict income_map[s] get()
            timing.append(timing_map.get(s))
        return timing



# end
