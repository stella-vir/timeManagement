# git create repo pages
# curl -u 'stella-vir' https://api.github.com/user/repos -d '{"name":"timeManagement"}'
# password: Personal access tokens
# repo url: https://github.com/stella-vir/timeManagement

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

    # def __str__(self):
    #     return self.schedules

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

        # [('Mon', '5:45'), ('Mon', '9:00')]
        for s in self.schedules:
            # tuple
            for sch, t in timing_map:
                #  _, t = timing
                if s == sch:
                    timing.append(t)
                    print('map', sch, t)

        return timing

    def get_date(self, date_map):
        date = []

        for s in self.schedules:
            # dict timing_map[s] == timing_map.get(s)
            date.append(date_map.get(s))
        return date








# end
