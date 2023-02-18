#!/usr/bin/env python3
# first you need to run daemon : $ sudo pigpiod
#to stop : $ sudo killall pigpiod

import smbus

rcatap_addr = 0x40
lcatap_addr = 0x41

i2c = smbus.SMBus(1)

i2c.write_byte_data(lcatap_addr, 0x01,0b00000000)

def forward():
    i2c.write_byte_data(lcatap_addr, 0x01,0b00000000)
    i2c.write_byte_data(rcatap_addr, 0x01,0b10000000)

def backward():
    i2c.write_byte_data(lcatap_addr, 0x01,0b10000000)
    i2c.write_byte_data(rcatap_addr, 0x01,0b00000000)


def right():
    forward()
    i2c.write_byte_data(rcatap_addr, 0x00, 0x80)
    i2c.write_byte_data(lcatap_addr, 0x00, 0x50)

def left():
    forward()
    i2c.write_byte_data(rcatap_addr, 0x00, 0x50)
    i2c.write_byte_data(lcatap_addr, 0x00, 0x80)


def move(key, val=None):
    if key == "s":
        right()

    if key == "f":
        left()

    if key == "e":
        stop()
        forward()
        i2c.write_byte_data(rcatap_addr, 0x00, 0x80)
        i2c.write_byte_data(lcatap_addr, 0x00, 0x80)

    if key == "d":
        stop()
        backward()
        i2c.write_byte_data(rcatap_addr, 0x00, 0x80)
        i2c.write_byte_data(lcatap_addr, 0x00, 0x80)

    if key == "q":
        stop()

def stop():
    i2c.write_byte_data(rcatap_addr, 0x00, 0x00)
    i2c.write_byte_data(lcatap_addr, 0x00, 0x00)

while True:
    try:
        key = input("e;forward s;right f;left d;back :")
        move(key)
    except(KeyboardInterrupt):
        stop()
        print("OK")
        break
