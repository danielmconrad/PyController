import pytest
from . import Dualshock4


controller = Dualshock4()


class TestDualshock4(object):
    def test_init(self):
        assert True