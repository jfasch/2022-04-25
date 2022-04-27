from paho.mqtt import client
import json
import time


c = client.Client()
c.connect('localhost', 1883)

while True:
    time.sleep(3)
    event = {
        'version': 2,
        'timestamp': time.time(),
    }

    c.publish('/firma/lightbarrier-238', json.dumps(event))
