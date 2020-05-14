# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:29:17 2020

@author: David Armstrong-Major Individual Design Project-Smart Home Energy
Controller

@estabishment: University of Bath-Mechanical Engineering Department-Integrated
Design Engineering

"""

#------------------------------------------------------------------------------
"""
This code will download the image file from the H:Drive with the specific date,
time filename. The program will then apply image filters and using pytesseract
the digits from the image will be extracted. These digits will be the summed
meter reading for the meter's lifespan.
The reading and other data will be written to the csv file created from another
code which will then be saved to the H:Drive.
Finally, a powershell execution line will send the reading to the app.
"""
#------------------------------------------------------------------------------
#Import modules from open source libraries, used for file name and
#downloading

import requests
from datetime import date, datetime

#------------------------------------------------------------------------------
#Import modules from open source libraries, used for image processing

import cv2
import pytesseract
from matplotlib import pyplot as plt

from PIL import Image

#------------------------------------------------------------------------------
#Import modules from open source libraries, used for csv file manipulation

import csv

#------------------------------------------------------------------------------
#Import modules from open source libraries, used for execution of external
#programs

import subprocess

#------------------------------------------------------------------------------

TimeStamp = datetime.now()                                                     #timestamp to compare H:Drive for images taken within the last hour (most recent)           
Dated = TimeStamp.strftime("%d%m%Y")                                           #dd/mm/YY
Timed = TimeStamp.strftime("%H")                                               #hour of image capture that filename was set to, note not set to hour an minute for demonstration purposes

#Creates a string with the date and time combined to match that of the filename
#which is on the H:Drive. For debugging purposes this was printed next to a 
#correctly formatted print command (print(Dated,Timed)) that cannot be 
#processed to the file path name directly
print(Dated,Timed)
Name1 = Dated 
Name2 = Timed
Name3 = str(Name1)+' '+str(Name2)                                              #combine the value of Name1 and Name2 variables into one single string 
print(Name3)

req = requests.get('https://people.bath.ac.uk/da491/Smart-Energy-Module/Meter Image Uploads/'+str(Name3)+'.jpg', stream=False)       #get request to download the meter image file

downloaded_file = open("H Drive Image.jpg", "wb")                              #open the image file with write formatting to allow for processing                       

for chunk in req.iter_content(chunk_size=256):                                 #reads the download file in chunks of 256 bytes to stop errors from larger files                   
    if chunk:                                                                  #if the chunk is true the it will write the file to the variable downloaded_file
        downloaded_file.write(chunk)
  
#------------------------------------------------------------------------------

downloaded_file = Image.open('H Drive Image.jpg')                              #save and open the image file to the local directory that the code is run from                       

rot = downloaded_file.rotate(-0.25)                                            #rotate the H:Drive image file by -0.25 degrees to compensate skew         
  
print(rot.size)                                                                # Image size, in pixels. The size is given as a 2-tuple (width, height).   

box = (800,500,1500,800)                                                       #set the left, top, right and bottom pixel coordinates
crop = rot.crop(box)                                                           #crop the rotated image to the pixel coordinates specified in the variable box

crop.save("Cropped Image.jpg")                                                 #save cropped image to allow it to be reloaded with different formatting    

img = cv2.imread('Cropped Image.jpg', 1)                                       #load the image file with cv2 open source library formatting, aligning with gray filtering formats and OCR              

gray_filtered = cv2.bilateralFilter(img, 40, 17, 17)                           #blur the image to reduce noise
                      
plt.subplot(121),plt.imshow(downloaded_file, cmap = 'gray')                    #set plot coordinates for original image without processing                                
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(gray_filtered,cmap = 'gray')                       #set plot coordinates for gray filtered image post processing for comparison                              
plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])

plt.show()                                                                     #display plots in software plot window for debugging

Reading = pytesseract.image_to_string(gray_filtered, config='output digits')   #call tesseract OCR software to read gray filtered image, read only digits and no text
print(Reading)

#------------------------------------------------------------------------------

UserID = 1234

Date = TimeStamp.strftime("%d/%m/%Y")
Time = TimeStamp.strftime("%H:%M:%S")

Data = [UserID,Date,Time,Reading]                                              #create an array with teh UserID, image date and time of capturing and the extracted meter reading       

with open('Meter Readings Data.csv', 'a', newline='') as file:                 #open the csv file with the name 'Meter Readings Data' with the format set to append                    
    writer = csv.writer(file)
    writer.writerow([UserID, Date, Time, Reading])                             #write in the first available row the value of the variables UserID, Date, Time and Reading                        

#------------------------------------------------------------------------------

csvload = {
    'filetwo': open('Meter Readings Data.csv', 'rb')                           #open the csv file that is saved on the local hard drive (created by CSV python code) to the variable csvload, format set to read file                          
}

try:
  res = requests.post(
    'https://people.bath.ac.uk/da491/Smart-Energy-Module/PostCSV.php',         #request for the php script that is saved on the H:Drive server 
    files = csvload                                                            #set the files to be uploaded to the csv variable
  )
  
  print(res.status_code)                                                       #print the execution status code that relates to a success or specific error for debugging
  
except requests.exceptions.RequestException as e:                              #print the error text if the request post was not successful
  print(e)

#If response of request is 1 (true) then print success message, if not print 
#error message to the console in plain english for any user to understand  
if res:
    print('CSV file upload successful.')
else:
    print('An error has occurred. CSV file upload unsuccessful!')

#------------------------------------------------------------------------------

subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./Live Gauge\";"])        #call for the powershell script to be executed

#------------------------------------------------------------------------------