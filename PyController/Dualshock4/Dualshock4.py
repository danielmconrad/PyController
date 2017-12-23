import hid


VENDOR_ID = 1356 # 1356 == 0x054c
PRODUCT_ID = 2976 # 2976 == 0x0ba0


class Dualshock4(object):
    def __init__(self):
        self._open_connection()

    def _open_connection(self):
        try:
            self._device = hid.device()
            print(hid.enumerate(VENDOR_ID, PRODUCT_ID))
            self._device.open(VENDOR_ID, PRODUCT_ID)
        except Exception as e:
            print("Unable to open device:", e)

    def read_input(self):
        return self._device.read(64)

    def yield_input(self):
        while True:
            yield self.read_input()
