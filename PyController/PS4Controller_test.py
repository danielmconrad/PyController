import pytest
from . import PS4Controller


controller = PS4Controller.PS4Controller()


class TestPS4Controller(object):
    def test_init(self):
        assert controller.device_identifier == "DUALSHOCK®4"

    def test_is_button_activated(self):
