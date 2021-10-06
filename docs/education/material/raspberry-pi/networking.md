# Networking with a Raspberry PI

## MQTT

### Mosquitto

!!! warning "WIP"
    Not yet

### Python

We can use Python and paho-mqtt client. Some examples [here](https://mntolia.com/mqtt-python-with-paho-mqtt-client/). This option can be used if you don't have a wifi capable module and you have a normal arduino that can send data over serial to your computer. This code example will go in your computer (we don't provide code for the arduino here)

#### Read serial data from your arduino

```
--8<-- "education/material/raspberry-pi/assets/snippets/serial_read_python.py"
```

#### Hello world to the MQTT broker

```
--8<-- "education/material/raspberry-pi/assets/snippets/mqtt_hello_python.py"
```

#### Code example

```
--8<-- "education/material/raspberry-pi/assets/snippets/mqtt_serial_python.py"
```

## References

- [Setting MQTT, node-red and more on a pi](https://gist.github.com/xoseperez/e23334910fb45b0424b35c422760cb87#file-rpi3_iot_server-md)
- [Securing the pi](https://www.raspberrypi.org/documentation/configuration/security.md)
- [MQTT users](http://www.steves-internet-guide.com/download/mosquitto-username-and-password-authentication/)
- [Python paho-mqtt examples](https://github.com/eclipse/paho.mqtt.python/blob/master/examples)