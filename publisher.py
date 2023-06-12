#encodeUTF8
#main script IOT Micromaster Curtin university 
#Capstone project BORDON Clement 07.06.23


import network
import datetime
import time
from machine import Pin
from umqtt.simple import MQTTClient
import os
import paho.mqtt.client as mqtt


class Pico_detection:
    def __init__(self):
        self.WIFI_AP = os.environ.get("WIFI_AP")        #Wifi SSID from localenv variable
        self.WIFI_PASSWD = os.environ.get("WIFI_PASSWD")    #Wifi passwd form local env variable
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
       
  
        self.SENSOR1 = Pin(16, Pin.IN)  #Sensors connexion signal the sensors should be connect to 5v power supply too
        self.SENSOR2 = Pin(10, Pin.IN)
        self.SENSOR3 = Pin(11, Pin.IN)
        self.SENSOR4 = Pin(12, Pin.IN)

        self.mqtt_server = '10.XXX.XXX.XXX'
        self.client_id = 'Object_nb0'
        self.topic_pub = 'detection'
        self.topic_msg = f'alert on {self.client_id} {datetime.datetime.now()}'

    def connection(self):
        self.wlan.connect(self.WIFI_AP,self.WIFI_PASSWD) #Wifi connection
        
        client = MQTTClient(client_id, mqtt_server, keepalive=3600) #MQTT connexion
        client.connect()
        print('Connected to %s MQTT Broker'%(mqtt_server))
        return client

    def reconnect(self):
        print('Failed to connect to the MQTT Broker. Reconnecting...')
        time.sleep(5)
        machine.reset()
    





