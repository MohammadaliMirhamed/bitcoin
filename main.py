# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 14:27:12 2018

@author: mohammadali
"""
import requests
import json
import time
import matplotlib.pyplot as plt



run = input("Start? > ")
mins = 0;lastprice = 0
listchart=[];listmin=[]
count=0;last_min_time=0

# Only run if the user types in "start"
if run == "start":
    # Loop until we reach 20 minutes running
    while mins<50:
        #send request to api 
        content = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json/")
        #convert the request content to json obj
        parsed = json.loads(content.text)
        #print second and price of bitcoin in USD
        print(str(mins)+" ==> "+str(parsed['bpi']['USD']['rate_float']))
        #check the price and alarm to client for sell or buy your bitcoin
        if lastprice>parsed['bpi']['USD']['rate_float']:
          print("Time To Buy")
        elif lastprice<parsed['bpi']['USD']['rate_float']:
          print("Time To Sell")
         #####
         
        lastprice = parsed['bpi']['USD']['rate_float']
        
        listchart.append(parsed['bpi']['USD']['rate_float'])
        listmin.append(mins)
        
        count+=1
        
        if count==10:
#            plt.subplot(1, 1, 1)
            for x in range(len(listchart)):
                
                plt.plot(listmin[x],((listchart[x])/2), 'o') 
            #set chart X,Y Title
            plt.xlabel('time (s)')
            plt.ylabel('Dollrs')
            #set title of chart
            plt.title('bitcoin realtime chart')
            
            plt.axis([last_min_time, mins, 0, lastprice])       
            #show the chart
            plt.show()     
            #claer listchart and listmin and count for making new chart
            listchart.clear()
            listmin.clear()   
            count=0
            #move lastest min to last_min_time for make chart from this time tile now
            last_min_time=mins
        
        # Sleep for a minute
        time.sleep(0.5)
        # Increment the minute total
        mins += 1
    # Bring up the dialog box here
    
