# iot-scripts
Scripts written in Python for devices to push data

Temp
The DS18B20 temp sensor uses the 1-wire interface.

	https://pinout.xyz/pinout/1_wire

To enable the one-wire interface you need to add the following line to /boot/config.txt, before rebooting your Pi:

	dtoverlay=w1-gpio

This assumes the use of the BCM4 pin (physical pin 7) but if you wish to use another pin: 

	dtoverlay=w1-gpio,gpiopin=x

In the latest PCB design, I use GPIO21 so I have to do this.
