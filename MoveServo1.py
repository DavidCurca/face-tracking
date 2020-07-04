import serial
import time

#workin!!
ser = serial.Serial('COM4', 9800, timeout=1)

for i in range(10):
        time.sleep(1)
        ser.write(b'80 110')   # send the pyte string 'H'
        time.sleep(1)   # wait 0.5 seconds
        ser.write(b'170 170')   # send the byte string 'L'

print("done")
