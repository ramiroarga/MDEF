# MQTT

**MQTT** was developed by Andy Stanford-Clark (IBM) and Arlen Nipper (Eurotech; now Cirrus Link) in 1999 for the monitoring of an oil pipeline through the desert. 

The goals were to have a protocol, which is bandwidth-efficient and uses little battery power, because the devices were connected via satellite link and this was extremely expensive at that time.

The protocol uses a publish/subscribe architecture wich is event-driven and enables messages to be pushed to clients. The central communication point is the MQTT broker, it is in charge of dispatching all messages between the senders and the rightful receivers. Each client that publishes a message to the broker, includes a topic into the message.

The topic is the routing information for the broker. Each client that wants to receive messages subscribes to a certain topic and the broker delivers all messages with the matching topic to the client. Therefore the clients don’t have to know each other, they only communicate over the topic. 

This architecture enables highly scalable solutions without dependencies between the data producers and the data consumers.

[Source](https://www.hivemq.com/blog/how-to-get-started-with-mqtt)

![](https://www.survivingwithandroid.com/wp-content/uploads/2016/10/mqtt_publisher_subscriber-1.png)

A topic is a simple string defined by the user that can have more hierarchy levels, which are separated by a slash. 

```
input/antonio/temperature
ouput/pepito/motor
```

Wilcards can also be used in sigle leves ej. `input/+/temperature` will return **temperatures of all users**.
Or in multilevels: `output/#` will return **all** outputs from **all users**.

!!! Note "Do it yourself"
    If you want to **make your own Raspberry PI - MQTT/Node-red server**, go here! [https://gitlab.com/fablabbcn-projects/learning/multinetworking/-/tree/master](https://gitlab.com/fablabbcn-projects/learning/multinetworking/-/tree/master)

## Use cases

We use MQTT in the [SmartCitizen Project](https://docs.smartcitizen.me) for sending data from the devices (the sensors) to our platform. You can find more info about this real-world case scenario in the [docs](https://docs.smartcitizen.me/Data/Sensor%20Platform)

## Examples

As you can imagine, MQTT can be used through many ways. Here is a compilation of some

!!! example "Embedded guides"
    Using MQTT on an embedded device:

    - [Using MQTT on an ESP32 - PubSubClient](/guides/embedded/esp32#mqtt)
    - [Using MQTT on an ESP8266 - PubSubClient](/guides/embedded/esp8266#mqtt)

!!! example "Raspberry PI or normal computer"
    - [Using MQTT with python on a Raspberry PI](/guides/raspberry-pi/networking#mqtt)
    - [Using MQTT with mosquitto on a Raspberry PI](/guides/raspberry-pi/networking#mosquitto)

## References

- [HiveMQ - Getting started with MQTT](https://www.hivemq.com/blog/how-to-get-started-with-mqtt)
- [MQTT users](http://www.steves-internet-guide.com/download/mosquitto-username-and-password-authentication/)