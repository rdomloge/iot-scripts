import requests
import sys
import json
import socket
import datetime
import sendemail

url_base = 'http://10.0.0.10:8123'


def record(url_path, k, v, source):
    url = url_base + url_path
    data = { }
    data["source"] = source
    data["hostname"] = socket.gethostname()
    data["time"] = datetime.datetime.utcnow().isoformat()
    data[k] = v;

    jsonStr = json.dumps(data);
    doRestCallWithExceptionHandling(url, jsonStr, k)

def doRestCallWithExceptionHandling(url, jsonStr, k):
    print("Data: "+jsonStr); 
    try:
        response = requests.post(url, data=jsonStr)
        print("Result: "+str(response.status_code));
        print("Msg: "+response.text);
    except:
        print("Could not record result: ", sys.exc_info()[0]);
        sendemail.send('rdomloge@gmail.com', 'rdomloge@gmail.com', 'Can''t connect to IOT endpoint - '+k, 'Help!')
    
