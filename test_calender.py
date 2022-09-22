from calender import Calender


def test_can_add_schedule_to_calender():
    s = Calender()
    s.add('week_days': 'Tue')
    assert s.size() == 1
