# git create repo pages
# curl -u 'stella-vir' https://api.github.com/user/repos -d '{"name":"timeManagement"}'

class Calender:
    def __init__(self):
        pass
    def add(self, schedule):
        dict = {
            'weeks': [0, 1],
            'week_days': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            'start_time': ['4:45', '9:00', '12:30'],
            'end_time': ['13:15', '16:30', '20:00']
            }

    def size(self):
        return 0

    def get_schedules(self):
        pass

    def get_gross_income(self):
        pass
