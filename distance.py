#!/usr/bin/python
import os
import time
import sys
import signal

import VL53L1X


tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
tof.open()
tof.start_ranging(1)
distance_mm =  tof.get_distance()

tof.stop_ranging()

print( distance_mm )

