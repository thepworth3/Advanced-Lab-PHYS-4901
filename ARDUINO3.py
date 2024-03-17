#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:48:28 2024

@author: portiaswitzer
"""

import numpy as np
import pyvisa
import array
import sys, time, os, csv, serial
rm = pyvisa.ResourceManager()
rm.list_resources()
print('RM',rm.list_resources())

inst = rm.open_resource('USB0::0x1AB1::0x0E11::DP8C192903387::INSTR') #what something is called (power source?)

ard=serial.Serial(port='/dev/cu.usbmodem141401', baudrate=9600) #port for the arduino
#ms=[]
curr=[]
current=[0,0.5,1,1.5,2,2.5,3,0] #and the average of the two zeros is the base [0,123450] should see 2 mT change between 1 and 5 (otherwise other cord)
B=[]
S=[]
#B=np.array(Bav)
 #.T
curr=np.array(curr)
current=np.array(current)

for i in current:
    inst.write(':APPLy CH1,{},{}'.format(30,i)) #writes 10V and 3 Amps

    
    time.sleep(1) #sleep for a bit to let the change happen 
    
    curr=np.append(curr,float(inst.query(':MEASure:CURRent? CH1').rstrip('\n')))
    
    time.sleep(1)
    
    ms=[]
    ms=np.array(ms)
    
    for k in range(10): #now take mag field measurements (10)
        
        ms=np.append(ms,float(str(ard.readline(),'UTF-8'))) #converts what the arduino is
        
        time.sleep(1)
        print('ms=',ms)
        
    Bavg=np.mean(ms)
    B.append(Bavg)
    Sd=np.std(ms)
    S.append(Sd)
    
print('B=',B)    
print('Stdev=',S)
print('curr',curr)
print('magsensor=',Bavg)
ard.close()
inst.close()

S=S/np.sqrt(10)

data=np.array([curr,B,S]).T
print('data=',data)

with open('Ten(cm).csv', 'w+', newline='') as bd:
     basicwriter=csv.writer(bd, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
     basicwriter.writerow(["Current (A)","B Average (mT)","SDOM"])
     basicwriter.writerows(data)


