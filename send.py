import requests
import sys
import json
import socket
import datetime

if(len(sys.argv) < 3):
    print("Please provide args [SOURCE] [TEMP]");
else:
    print("Args: "+str(sys.argv));
    url = 'http://10.0.0.14:8080/temperatureReadings'
    data = {
            "source": None,
            "temp": None,
            "time": None,
            "hostname": None
            }
    data["source"] = sys.argv[1];
    data["temp"] = sys.argv[2];
    data["hostname"] = socket.gethostname()
    data["time"] = datetime.datetime.utcnow().isoformat()
    jsonStr = json.dumps(data);
    print("Data: "+jsonStr); 
    response = requests.post(url, data=jsonStr)
    print("Result: "+str(response.status_code));
    print("Msg: "+response.text);
