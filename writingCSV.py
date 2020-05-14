# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:22:56 2020

@author: David Armstrong-Major Individual Design Project-Smart Home Energy
Controller

@estabishment: University of Bath-Mechanical Engineering Department-Integrated
Design Engineering

"""
#------------------------------------------------------------------------------
"""
This code will create a csv file on the local server with the headings
UserID, Data, Time and Reading. Once the image processing is complete
the data will be written to this file
"""
#------------------------------------------------------------------------------
#Import modules from open source libraries, user for csv file manipulation
#and current date and time stamping
 
import csv                                                                       
from datetime import date, datetime                                                                       

#------------------------------------------------------------------------------

with open('Meter Readings Data.csv', 'w', newline='') as file:                 #create and open the csv file with the name 'Meter Readings Data' and save the variable as 'file'                                                      
    writer = csv.writer(file)                                                                    
    writer.writerow(["UserID", "Date", "Time","Reading"])                      #whilst the csv file is open write the row containing the heading titles                                                      
