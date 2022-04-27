#import barcode_reader_X3452
import barcode_reader_Y1234

from paho.mqtt import client
import json


reader = barcode_reader_Y1234.Barcode_Y1234()

c = client.Client()
c.connect('localhost', 1883)

def event_received(client, userdata, event):
    event = json.loads(event.payload)
    ts = event['timestamp']
    code = reader.get_code()
    print(f'Event at {ts}, code was {code}')

c.on_message = event_received

c.subscribe('/firma/lightbarrier-238')
c.loop_forever()
