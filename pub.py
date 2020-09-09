import paho.mqtt.client as mqtt
import time

Mc = mqtt.Client()
Mc.connect("158.108.112.39", 1883)

while True:
    Mc.publish("TEST/SS", "on")
    time.sleep(2)