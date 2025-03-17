import os #importing a library into your code

#print(os.system('systeminfo')) #running a command in the terminal


#print(os.system('systeminfo | find "System Boot Time"'))

print(os.system('date /t ')) #/t is a flag that tells the date command to only display the date and not the time

print(os.system('time /t ')) #/t is a flag that tells the time command to only display the time and not the date

