import requests
import sys
import json
import socket
import datetime

    

def send(distance_mm, source):
    distance_cm = int(distance_mm) /10
    url = 'http://10.0.0.14:8080/distanceReadings'
    data = {
            "source": None,
            "distance_cm": None,
            "time": None,
            "hostname": None
            }
    data["source"] = source
    data["distance_cm"] = str(distance_cm)
    data["hostname"] = socket.gethostname()
    data["time"] = datetime.datetime.utcnow().isoformat()
    jsonStr = json.dumps(data);
    print("Data: "+jsonStr); 
    response = requests.post(url, data=jsonStr)
    print("Result: "+str(response.status_code));
    print("Msg: "+response.text);



if(len(sys.argv) < 3):
    print("Please provide args [SOURCE] [DISTANCE_CM]");
else:
    print("Args: "+str(sys.argv));
    send(sys.argv[2], sys.argv[1])

