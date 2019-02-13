import RPi.GPIO as GPIO
import time, sys
f = open('FlowMeterOutput.txt', 'a')

GPIO.setmode(GPIO.BOARD)
inpt = 13
GPIO.setup(inpt, GPIO.IN)
minutes = 0
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
f.write('\nWater Flow - approximate - Reports every ' +
        str(rpt_int)+' Seconds  '+
        str(time.asctime(time.localtime(time.time()))))

while True:
    time_new = time.time()+rpt_int
    rate_cnt = 0
    while time.time() <= time_new:
        try:
            None
            #print(GPIO.input(inpt), end='')
            GPIO.input(inpt)
        except KeyboardInterrupt:
            print('CTRL-C - exiting')
            GPIO.cleanup()
            f.close()
            print('Done')
            sys.exit()

    minutes += 1

    LperM = round(((rate_cnt*constant)/(rpt_int/60)),2)
    TotLit = round(tot_cnt * constant,1)
    print('\nLitres / min ', LperM, '(',rpt_int, ' second sample)')
    print('Total litres ', TotLit)
    print('Time (min & clock) ', minutes, '\t',
            time.asctime(time.localtime(time.time())), '\n')
    f.write('\nLitres / min ' + str(LperM))
    f.write('  Total litres ' + str(TotLit))
    f.write('  Tie (min & clock) ' + str(minutes) + '\t' +
            str(time.asctime(time.localtime(time.time()))))
    f.flush()

GPIO.cleanup()
f.close()
print('Done')
