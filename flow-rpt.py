#!/usr/bin/python3
import RPi.GPIO as GPIO
import time, sys
import sendemail

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

GPIO.add_event_detect(inpt,GPIO.FALLING,
        callback=Pulse_cnt,bouncetime=10)

# MAIN
print('Water Flow - approximate ',
        str(time.asctime(time.localtime(time.time()))))
rpt_int = int(input('Input desired report interval in seconds '))
print('Reports every ', rpt_int, ' seconds')
print('CTRL-C to exit')

while True:
    time_new = time.time()+rpt_int
    rate_cnt = 0
    while time.time() <= time_new:
        try:
            None
            #print(GPIO.input(inpt), end='')
            GPIO.input(inpt)
            time.sleep(0.1)
        except KeyboardInterrupt:
            print('CTRL-C - exiting')
            GPIO.cleanup()
            print('Done')
            sys.exit()

    LperM = round(((rate_cnt*constant)/(rpt_int/60)),2)
    if(LperM > 0): 
            sendemail.send('rdomloge@gmail.com', 'rdomloge+flow-iot@gmail.com', 'Flow detected', 'Flow:'+str(LperM))
    TotLit = round(tot_cnt * constant,1)
    print('\nLitres / min ', LperM, '(',rpt_int, ' second sample)')
    print('Total litres ', TotLit)

GPIO.cleanup()
print('Done')
