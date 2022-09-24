arduino-cli compile -b arduino:avr:uno ControlSketch
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno ControlSketch
