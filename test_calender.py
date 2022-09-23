from calender import Calender
from schedule_database import ScheduleDatabase
import pytest
from unittest.mock import MagicMock


@pytest.fixture
def s():
    # s = Calender(5)
    return Calender(5)


def test_can_add_schedule_to_calender(s):
    # s.add({'week_days': 'Tue'})
    s.add('Tue')

    assert s.size() == 1

def test_when_schedule_added_then_calender_contains_schedule(s):
    # s.add({'week_days': 'Tue'})

    # add 6 0-5 6 times overflow #add 5 0-4 5 times not overflow
    # pre-fill 5 items
    for _ in range(5):
        s.add('Tue')
    # raises error ONLY on the 6th
    # should pass the test on error, if not, code bugs
    with pytest.raises(OverflowError):
        s.add('Tue')

    assert 'Tue' in s.get_schedules()


# >> pytest test_calender.py::test_can_get_gross_income -s
def test_can_get_timing(s):
    # print('Print test_can_get_gross_income ONLY')
    s.add('Tue')
    s.add('Sat')

    '''
    timing_map = {
        'Tue': '5:45',
        'Sat': '9:00',
    }
    '''

    schedule_database = ScheduleDatabase()
    # schedule_database.get = MagicMock(return_value = ['5:45', '9:00'])

    def mock_get_timing(schedule):
        if schedule == 'Tue':
            return '5:45'
        if schedule == 'Sat':
            return '9:00'
    schedule_database.get = MagicMock(side_effect = mock_get_timing)

    # assert '9:00' in s.get_timing(timing_map)
    print(s.get_timing(schedule_database))
    assert '9:00' in s.get_timing(schedule_database)











# end
