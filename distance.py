#!/usr/bin/python
import os
import time
import sys
import signal
import time

import VL53L1X

attempts = 20;


def calcAvgDistance():
    tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
    tof.open()
    tof.start_ranging(1)
    totalDistance = 0
    samples = 0
    for x in range(attempts):
        measured = tof.get_distance()
        print("Measured "+str(measured))
        time.sleep(1)

        if x > 3:
            samples += 1
            totalDistance += measured
            print(".")

    tof.stop_ranging()
    return totalDistance / samples

def main():
    print("Time of Flight")
    distance = calcAvgDistance()
    print("Distance: {}mm".format(distance))
    sys.stderr.write(str(distance)+'\n')

if __name__ == '__main__':
    main()

