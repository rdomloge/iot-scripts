#!/usr/bin/python3
import distance
import sendDistance

distance = distance.calcAvgDistance()
sendDistance.send(distance, 'pi0')

