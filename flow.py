#!/usr/bin/python3

import RPi.GPIO as GPIO
import time, sys, socket, datetime, requests, json
import sendemail
import record_value

GPIO.setmode(GPIO.BCM)
inpt = 25
GPIO.setup(inpt, GPIO.IN)
constant = 0.006
time_new = 0.0
rpt_int = 10

global rate_cnt, tot_cnt
rate_cnt = 0
tot_cnt = 0

def Pulse_cnt(inpt_pin):
    global rate_cnt, tot_cnt
    rate_cnt += 1
    tot_cnt += 1

def sendFlow(lpm):
    record_value.record('/flowReadings', 'flowLpm', lpm, 'Pi0')

GPIO.add_event_detect(inpt,GPIO.FALLING,
        callback=Pulse_cnt,bouncetime=10)

# MAIN
rpt_int = 300
print('Reports every ', rpt_int, ' seconds. CTRL-C to exit')

while True:
    rate_cnt = 0
    try:
        None
        time.sleep(rpt_int);
    except KeyboardInterrupt:
        print('CTRL-C - exiting')
        GPIO.cleanup()
        print('Done')
        sys.exit()

    LperM = round(((rate_cnt*constant)/(rpt_int/60)),2)
    if(LperM > 0):
        sendemail.send('rdomloge@gmail.com', 'rdomloge+flow-iot@gmail.com', 'Flow event', 'Flow: '+str(LperM))
    if(rate_cnt > 0 and LperM == 0):
        sendemail.send('rdomloge@gmail.com', 'rdomloge+false-reading@gmail.com', 'False flow', 'Flow reader read {} which rounds to zero.'.format(rate_cnt))
    TotLit = round(tot_cnt * constant,1)
    print('\nLitres / min ', LperM, '(',rpt_int, ' second sample)')
    sendFlow(LperM);

GPIO.cleanup()
print('Done')
