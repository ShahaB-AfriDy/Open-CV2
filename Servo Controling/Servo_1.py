# import RPi.GPIO as GPIO
# import time

# servoPIN = 17

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(servoPIN, GPIO.OUT)

# p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
# p.start(2.5) # Initialization
# try:
#   while True:
#     p.ChangeDutyCycle(5)
#     time.sleep(0.5)
#     p.ChangeDutyCycle(7.5)
#     time.sleep(0.5)
#     p.ChangeDutyCycle(10)
#     time.sleep(0.5)
#     p.ChangeDutyCycle(12.5)
#     time.sleep(0.5)
#     p.ChangeDutyCycle(10)
#     time.sleep(0.5)
#     p.ChangeDutyCycle(7.5)
#     time.sleep(0.5)
#     p.ChangeDutyCycle(5)
#     time.sleep(0.5)
#     p.ChangeDutyCycle(2.5)
#     time.sleep(0.5)
# except KeyboardInterrupt:
#   p.stop()
#   GPIO.cleanup()





List = [20, 6, 23, 19, 9, 14, 15, 3, 1, 12, 10, 20, 13, 3, 17, 10, 11, 6, 21, 9, 6, 10, 9, 4, 5, 1, 5, 11, 7, 24]
List = sorted(List)
import numpy as np
List = np.array(List).reshape(6,5)

from pandas import DataFrame
DF = DataFrame(data=List,columns=['0-5','5-10','10-15','15-20','20-25'])
print(DF)


# print(List)
# List = list(filter(lambda x:25>x>=20,List))
# print("\n")
# print(len(List))