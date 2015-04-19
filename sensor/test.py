#!/usr/bin/python
 
import spidev
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
spi2 = spidev.SpiDev()
spi2.open(0,1)


# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel1(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data


def ReadChannel2(channel):
  adc = spi2.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Define sensor channels
light_channel = 0
temp_channel  = 1
 
# Define delay between readings
delay = 5
 
while True:
 
  for x in range(0,8):
	value1 =	ReadChannel1(x)
	value2 = 	ReadChannel2(x)
	print('Channel: {0} Value1:{1} Value2:{2}'.format(x,value1,value2)) 
  print('##############################################')
  time.sleep(delay)
  
