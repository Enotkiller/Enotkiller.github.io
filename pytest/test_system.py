import pytest, sys, os
from random import randint
sys.path.append(r"C:\Users\Enot\PycharmProjects\ideya-pidora\code")
import System 
class TestSystem():
    def setup_method(self):
        self.system = System.system()
        
    def test_get_day_weekly_now(self):
        assert self.system.get_day_weekly_now() in [1, 2, 3, 4, 5, 6, 7]
    
    @pytest.mark.parametrize("now,day,mounth,_mounth,_day,result", [
        (1, 1, 9, 9, 2, 1),
        (1, 1, 9, 9, 8, 0),
        (0, 1, 9, 9, 8, 1),
        (1, 6, 1, 4, 3, 1),
        (0, 14, 7, 11, 28, 1)
    ])
    def test_get_week_type(self, now, day, mounth, _mounth, _day, result):
        assert self.system.get_week_type(now = now, day = day, mounth = mounth, _mounth = _mounth, _day = _day, _year = 2025) == result
    
    @pytest.mark.parametrize("mounth,day", [(randint(1, 12), randint(1, 28)) for i in range(10)])
    def test_get_day_weekly(self, mounth, day):
        assert self.system.get_day_weekly(mounth = mounth, day = day) in [1, 2, 3, 4, 5, 6, 7]
    
    def test_get_time_float(self):
        assert 0 < self.system.get_time_float() < 24
        assert self.system.get_time_float() % 1 <= 59