# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:54:35 2020

@author: David Armstrong-Major Individual Design Project-Smart Home Energy
Controller

@estabishment: University of Bath-Mechanical Engineering Department-Integrated
Design Engineering

"""
#------------------------------------------------------------------------------
"""
This code will be executed on a raspberry pi board. It will image an LCD
display that acts as a digital meter display. An LED will light as the camera
takes the image acting as a light source for imaging in dark conditions.
The code then calls a .php script and passed the image file to be sent to a
personal H:Drive
"""
#------------------------------------------------------------------------------
#Import modules from open source libraries, used for raspberry pi camera
#capturing

from picamera import PiCamera

#------------------------------------------------------------------------------
#Import modules from open source libraries, used for raspberry pi pin selection

import RPi.GPIO as GPIO   

#------------------------------------------------------------------------------                                                  
#Import modules from open source libraries, used for date and time stamping

import datetime
from time import sleep
from datetime import date, datetime

#------------------------------------------------------------------------------
#Import modules from open source libraries, used for sending files to H:Drive

import requests

#------------------------------------------------------------------------------

UserID = 1234                                                                  #homeowners personal ID number to be tagged with the photo     

#Initialise the camera and calibrate the settings
camera = PiCamera()                                                                       
camera.resolution = (1980,1080)                                                                       
camera.sharpness = 100                                                                       
camera.contrast = 75                                                                       
camera.exposure_mode = 'backlight'                                                                       


LED = 40                                                                       #set pin number that the LED is wired to as per board, GPIO21 as per BCM

GPIO.setwarnings(False)                                                        #disable warnings
GPIO.setmode(GPIO.BOARD)                                                       #set pin numbering format to be used by the board
GPIO.setup(LED, GPIO.OUT)                                                      #set GPIO as output

camera.start_preview()                                                         #display the camera's view on the raspberry pi display              
GPIO.output(LED, GPIO.HIGH)                                                    #set pin 40 (LED) to high                   
print ("LED On")                                                               #feedback to user that LED is on symbolising image is being taken        
    
sleep(5)
    
Image = camera.capture('/home/pi/Desktop/LCDImage.jpg')                        #capture image and save it to the desktop with the filename 'LCDImage.jpg'                                               

TimeStamp = datetime.now()                                                     #timestamp the image                  
Date = TimeStamp.strftime("%d/%m/%Y")                                          # dd/mm/YY
Time = TimeStamp.strftime("%H:%M:%S")                                          # H:M:S
    
camera.stop_preview()                                                                       
GPIO.output(LED,GPIO.LOW)                                                                       
print ("LED Off")
    
sleep(5)
 
#Print image details   
print('Meter Image Taken')
print("Date of Picture:", Date)
print("Time of Picture =", Time)

#------------------------------------------------------------------------------

fupload = {
  'fileone' : open('/home/pi/Desktop/LCDImage.jpg', 'rb')                      #open the image file that is saved on the raspberry pi desktop to the variable fupload, format set to read file                              
}

d = {'UserID': UserID,'Date': Date,'Time': Time}                               #create an array of the UserID and image timestamp                                   

try:
  res = requests.post(
    'https://people.bath.ac.uk/da491/Smart-Energy-Module/PostHDrive.php',      #request for the php script that is saved on the H:Drive server     
    files = fupload,                                                           #set the files to be uploaded to the image variable       
    data = d                                                                   #set the data to be uploaded to the image data array
  )
  
  print(res.status_code)                                                       #print the execution status code that relates to a success or specific error for debugging           
  
except requests.exceptions.RequestException as e:                              #print the error text if the request post was not successful                                    
  print(e)

#If response of request is 1 (true) then print success message, if not print 
#error message to the console in plain english for any user to understand
if res:                                                                        
    print('Program Ran Correctly.')
else:
    print('An error has occurred.')