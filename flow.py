#!/usr/bin/python3

import RPi.GPIO as GPIO
import time, sys, socket, datetime, requests, json
import sendemail

GPIO.setmode(GPIO.BOARD)
inpt = 22
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

def sendFlow(lpm):
    url = 'http://10.0.0.14:8080/flowReadings'
    data = {
        "source": None,
        "distance_cm": None,
        "time": None,
        "hostname": None
    }
    data["source"] = 'Pi0'
    data["flow_lpm"] = lpm
    data["hostname"] = socket.gethostname()
    data["time"] = datetime.datetime.utcnow().isoformat()
    jsonStr = json.dumps(data);
    print("Data: "+jsonStr); 
    response = requests.post(url, data=jsonStr)
    print("Result: "+str(response.status_code));
    print("Msg: "+response.text);

GPIO.add_event_detect(inpt,GPIO.FALLING,
        callback=Pulse_cnt,bouncetime=10)

# MAIN
rpt_int = 300
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
            time.sleep(0.5);
        except KeyboardInterrupt:
            print('CTRL-C - exiting')
            GPIO.cleanup()
            print('Done')
            sys.exit()

    minutes += 1

    LperM = round(((rate_cnt*constant)/(rpt_int/60)),2)
    if(LperM > 0):
        sendemail.send('rdomloge@gmail.com', 'rdomloge+flow-iot@gmail.com', 'Flow event', 'Flow: '+str(LperM))
    TotLit = round(tot_cnt * constant,1)
    print('\nLitres / min ', LperM, '(',rpt_int, ' second sample)')
    sendFlow(LperM);

GPIO.cleanup()
print('Done')
