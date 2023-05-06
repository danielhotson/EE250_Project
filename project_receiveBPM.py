import time
import paho.mqtt.client as mqtt
import numpy as np

i = 0
bpm_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def on_connect(client, userdata, flags, rc):
    	client.subscribe("pi/bpm")
    	client.message_callback_add("pi/bpm", on_message_from_BPM)
    
    
def on_message_from_BPM(client, userdata, message):
    global i
    global bpm_arr
    bpm_avg = 0
    temp = int(message.payload.decode())
    if temp > 10:
    	if i < 9:
    	    bpm_arr[i] = temp
    	    i = i + 1
    	    print("calculating")
    	else:
   	    bpm_arr[i] = temp
   	    i = 0
   	    bpm_avg = np.mean(bpm_arr)
   	    print("Your heart rate is: ", round(bpm_avg), "BPM")
    else:
        print("heart rate not detected")
        i = 0
   	    
   	    

if __name__ == '__main__':
    
    client = mqtt.Client()
    print("Beginning Heart Rate Measurement")
    client.on_connect = on_connect
    client.connect(host="192.168.123.4", port= 1883, keepalive=60)
    client.loop_start()
    time.sleep(1)
    
    while True:
    	time.sleep(1)
        
