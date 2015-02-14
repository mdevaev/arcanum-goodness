#!/usr/bin/env python3


import struct
import serial


# =====
class ArcanumGoodness:
    def __init__(self, device):
        self._tty = serial.Serial(device, 9600)

    def set_gauge(self, value):
        self._send(0, value)

    def set_light(self, value):
        self._send(1, value)

    def _send(self, cmd, value):
        assert 0 <= value <= 255
        values = map(self._make_byte, (cmd, value))
        self._tty.write(struct.pack("<cc", *values))

    def _make_byte(self, value):
        return bytes([int(value)])


ac = ArcanumGoodness("/dev/ttyACM0")
import time; time.sleep(10)
ac.set_gauge(4)
ac.set_light(255)
time.sleep(5)
ac.set_gauge(150)
ac.set_light(150)
