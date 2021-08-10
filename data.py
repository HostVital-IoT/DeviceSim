from hashlib import new
import random
from tkinter.constants import E
import requests
from requests.api import options, request
import time

bp = 0
oxy = 0
sug = 0
name= ''

def newPatient(name):
    oxy = random.randint(90,100) #Oxygen level
    bp = random.randint(60,120) #Heartbeat  
    sug = random.randint(80,140)#Sugar  
    r = requests.post('https://iot--api.herokuapp.com/new/', json ={'name':name , 'blood_pressure':bp , 'sugar_level':sug, 'oxygen_level':oxy})
    print("Response from Server: ")
    print (r)


def updatePatient(id,name):
    oxy = random.randint(90,100) #Oxygen level
    bp = random.randint(60,120) #Heartbeat  
    sug = random.randint(80,140)#Sugar 
    link= 'https://iot--api.herokuapp.com/_id:'
    link= link + id
    r = requests.put(link, json ={'name':name , 'blood_pressure':bp , 'sugar_level':sug, 'oxygen_level':oxy})
    print("Response from Server: ")
    print (r)


print("HostVital Data Sim")
print("Type 1 to send new patient data or 2 to send data to an existing patient: ")
menuoption = int(input())
if menuoption == 1: 
    print("Enter Username: ")
    name= input()
    newPatient(name)
elif menuoption == 2:
    print("Enter ID: ")
    id=input()
    print("Enter Name: ")
    name=input()
    print("Do you want to update the data continuously? Type 1 for yes and 2 for no: ")
    decision = int(input())
    if decision==1:
        i=False
        print("Use CTRL+C to stop.")
        while i==False:
            updatePatient(id,name)
            time.sleep(5)
    else:
        updatePatient(id,name)

# send_data()

