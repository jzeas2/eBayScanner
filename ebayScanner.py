#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 18:06:12 2019
@author: jonathanzeas


This script allows users to continually search on eBay for an item they know will be listed soon.

Once the item is found, the pay window opens on the user's computer and all they must do is click the "pay now"
button and the specified quantity of the item will be purchased.

Great for sniping a deal before others have the chance to.
"""



import urllib
import webbrowser
import time


ure = 2
#get user input
kwd = input("Please enter the keyword you're searching for\n\n")
url = input("Please enter the URL you're searching for this keyword in\n\n")
qty = input("Please enter the quantity you'd like to purchase\n\n")
#loop until found
while ure < 3:
    #open url
    z = urllib.request.urlopen(url)
    try:
        #read session
        z = z.read()
    except:
        print("Error Searching")
        time.sleep(30)
    #convert to string
    z = str(z)
    #search for string in html code
    y = z.find(kwd)
    y = int(y)
    #if not found
    if y < 0:
        #sleep again and loop through
        print("Searching...")
        time.sleep(30)
    #otherwise, end the loop
    else:
        ure = 4


str1 = ""
#take all text around found text
for i in range (-100,200):
    str1 = str1 + z[y+i]
#search for url in str1
strap = str1.find("https://")
lenstr1 = len(str1)
str2 = ""
#put all char from str1 that are in & after https into a new variable
for i in range(0,lenstr1):
    if i >= strap:
        str2 = str2 + str1[i]
    else:
        str2 = str2
#find the end of url
strap2 = str2.find('"')
#define new variable as just the URL
str3 = str2[:strap2]
#open the URL
webbrowser.open(str3)

#find item number in URL
item_num_loc = z.find("item=")
item_num_end = z.find("&amp;",item_num_loc)
item_num = z[item_num_loc+5:item_num_end]
print(item_num)
#open "pay now" page in user's default web browser
webbrowser.open("https://pay.ebay.com/rxo?action=create&rypsvc=true&pagename=ryp&TransactionId=-1&item="+item_num+"&quantity="+qty)

