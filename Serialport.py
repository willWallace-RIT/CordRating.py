# On the ESP32/Arduino side:
# Measure voltage on analog pin and send via serial

import serial

ser = serial.Serial('COM3', 115200)  # Change COM port accordingly

while True:
    line = ser.readline().decode().strip()
    try:
        voltage = float(line)
        print(f"Voltage: {voltage:.2f} V")
    except:
        continue
