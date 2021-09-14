#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 08:48:53 2021

@author: nathanyoshino
"""
#import the libraries that we need, NumPy for mathematical operations and 
import numpy as np
import matplotlib.pyplot as plt


#Create a variable corresponding to the file name. This file must be uploaded to Google Colab. If working offline, this file must be in the same directory as the .py file. 
infile = "Day1CountryInfo2018.csv"

#Create empty lists to store our data
country_list = []
lat_list = []
long_list = []

#These lines open "infile", which we have assigned to our desired file name. 
#The "r" means we want to read this file.  
#This information is all saved as the variable "csv_file"
with open (infile, 'r') as csv_file:
    
    #The first line of the csv file is not important information for us, it's just the headers
    #The following command processes that first line so when we loop over the rest it's not included
    headers = csv_file.readline()
    
    #This for loop will iterate over all of the lines in "csv_file" which we assigned all of the data in the file to
    #ie, every iteration of the loop will be a different line
    for line in csv_file:

        #The split function will split up lines based on whatever you designate.
        #Here we are designating to split each line at the commas, creating three variables: a name, latitute, and longitude
        #These three variables are contained within the newly created "country_info" variable as a list       
        country_info = line.split(',')
        
        #The next three lines append each variable in "country_info" to one of the lists we created at the top
        #The values were read from a file, so all of these variables are strings
        #For the sake of plotting, we need them to be numbers, or floats more precisely
        #So for the latitude and longitude, we turned them into floats with the float() function
        country_list.append(country_info[0])
        lat_list.append(float(country_info[1]))
        long_list.append(float(country_info[2]))
        

print(country_list)
print(lat_list)
print(long_list)
#print out your lists to make sure they contain the correct data before continuing.

#The next line creates a new figure, important when you work with multiple plots
plt.figure()
#plot the x values (longitude) with the yvalues (latitude)
plt.scatter(long_list, lat_list)
plt.title("Map of Countries that Participated in the 2018 Winter Olympics")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
#mark the equator
plt.hlines(0,-150,200)
plt.show()
plt.savefig("Day_1_HW.png")
