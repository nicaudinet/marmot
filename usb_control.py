#!/usr/bin/env python3
"""Control an Arduino over the USB port."""

# usb.py
# Created by John Woolsey on 12/17/2019.
# Copyright (c) 2019 Woolsey Workshop.  All rights reserved.


# USB_PORT = "/dev/ttyUSB0"  # Arduino Uno R3 Compatible
USB_PORT = "/dev/ttyACM0"  # Arduino Uno WiFi Rev2


# Imports
import serial


# Functions
def print_commands():
   """Prints available commands."""
   print("Available commands:")
   print("  f - forward")
   print("  b - back")
   print("  l - left")
   print("  r - right")
   print("  x - exit")
   print("  s - stop")


# Main

# Connect to USB serial port at 9600 baud
try:
   usb = serial.Serial(USB_PORT, 9600, timeout=2)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit()

# Send commands to Arduino
print("Enter a command from the keyboard to send to the Arduino.")
print_commands()
while True:
   vel = input("Enter velocity: ")

   vel = 'speed' + str(vel)
   usb.write(bytes(vel, encoding='utf-8'))  # send command to Arduino

   command = input("Enter direction: ")

   if command == "f":  # read Arduino A0 pin value
      usb.write(b'forward')  # send command to Arduino
      print(f"Going forward with {vel}.")
      line = usb.readline()  # read input from Arduino
      line = line.decode()  # convert type from bytes to string
      print(f"got {line}")

   elif command == "b":  # turn on Arduino LED
      usb.write(b'back')  # send command to Arduino
      print(f"Going back with {vel}.")

   elif command == "l":  # turn off Arduino LED
      usb.write(b'left')  # send command to Arduino
      print(f"Turning left with {vel}.")

   elif command == "r":  # turn off Arduino LED
      usb.write(b'right')  # send command to Arduino
      print(f"Turning right with {vel}.")

   elif command == "s":  # turn off Arduino LED
      usb.write(b'stop')  # send command to Arduino
      print(f"Stopping.")

   elif command == "x":  # exit program
      print("Exiting program.")
      exit()
   else:  # unknown command
      print("Unknown command '" + command + "'.")
      print_commands()