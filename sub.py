import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
    client.subscribe('cpe5camp/at99/sftohw')
    if rc==0:
        print('connected')
    else:
        print('not connect')

def on_message(client,userdata,message):
    print('message '+str(message.payload.decode('utf-8')))
    print('message topic',message.topic)
    
host = '192.168.31.102'
port = 1883

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.connect(host,port=port,keepalive=60)

client.loop_forever()
