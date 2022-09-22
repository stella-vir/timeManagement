from calender import Calender


def test_can_add_schedule_to_calender():
    s = Calender()
    # s.add({'week_days': 'Tue'})
    s.add('Tue')

    assert s.size() == 1

def test_when_schedule_added_then_calender_contains_schedule():
    s = Calender()
    # s.add({'week_days': 'Tue'})
    s.add('Tue')

    assert 'Tue' in s.get_schedules()
