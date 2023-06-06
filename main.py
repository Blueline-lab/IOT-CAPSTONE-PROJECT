import network
import datetime
import time
#from machine import Pin
#from umqtt.simple import MQTTClient
import os

import paho.mqtt.client as mqtt



WIFI_AP = os.environ.get("WIFI_AP")
WIFI_PASSWD = os.environ.get("WIFI_PASSWD")
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_AP,WIFI_PASSWD)
time.sleep(5)


sensor1 = Pin(16, Pin.IN)
sensor2 = Pin(10, Pin.IN)

mqtt_server = '10.XXX.XXX.XXX'
client_id = 'Object_nb0'
topic_pub = 'detection'
topic_msg = f'Alert on {client_id} {datetime.datetime.now()}'

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
while True:
    if sensor1.value() == 0 or sensor2.value() == 0:
        client.publish(topic_pub, topic_msg)
        time.sleep(3)
    else:
        pass