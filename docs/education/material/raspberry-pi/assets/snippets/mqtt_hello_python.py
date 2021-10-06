import paho.mqtt.client as mqtt

mqtt_broker = "SERVERADDRESS"
mqtt_user = "MQTTUSER"
mqtt_pass = "MQTTPASS"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
   print("Connected With Result Code "+rc)

def on_message(client, userdata, message):
   print("Message Recieved: "+message.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker, broker_port)
client.username_pw_set(username = mqtt_user, password = mqtt_pass)

client.subscribe("output", qos=1)

client.publish(topic="input", payload="Hello from python", qos = 1, retain = False)

client.loop_forever()