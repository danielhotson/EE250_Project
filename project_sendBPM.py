from pulsesensor import Pulsesensor
import grovepi
import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    time.sleep(1)

if __name__ == '__main__':
    p = Pulsesensor()
    p.startAsyncBPM()
    i = 0
    sensor = 4

    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host="192.168.123.4", port= 1883, keepalive=60)
    
    client.loop_start()
    time.sleep(1)
    print("Publishing BPM and Temp")
    
    while True:
       bpm = round(p.BPM)
       client.publish("pi/bpm", f"{bpm}")
       if i > 10:
           [temp,humidity] = grovepi.dht(sensor,0)
           client.publish("pi/temp", f"{temp}")
           client.publish("pi/humidity", f"{humidity}")
           i = 0
       else:
           i = i + 1
       time.sleep(1)


