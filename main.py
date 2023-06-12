from publisher import Pico_detection

PICO = Pico_detection()

def main():
    try:
        client = PICO.connection()
    except OSError as e:
        PICO.reconnect()
    while True:
        if PICO.sensor1.value() == 0 or PICO.sensor2.value() == 0 or PICO.sensor3.value() or PICO.sensor4.value():
            PICO.client.publish(topic_pub, topic_msg)
            time.sleep(3)
        else:
            pass


run = main()
