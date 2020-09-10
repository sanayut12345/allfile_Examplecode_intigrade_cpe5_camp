from gpiozero import DistanceSensor
from time import sleep
import paho.mqtt.client as mqtt

#connection to mqtt
Mc = mqtt.Client()
Mc.connect("158.108.137.1", 1883)

#get distance from ul
sensor = DistanceSensor(echo=24, trigger=18, max_distance=2.0)

while True:
 distance = sensor.distance * 100
 print("Distance : " , distance)
 #code publush data to mqtt
 Mc.publish("cpe5camp/at99", str(distance))
 sleep(1)