#oprning and reading a file
file = open("C:\\Users\\kariu\\OneDrive\\Documents\\me.txt","r")
content = file.read()
print(content)

#delete a file
import os
os.remove("my_file.txt")

#create file and write into it
created_file = open("my_file.txt","x+")
file = open("my_file.txt","w+")
file.writelines(["\nBEnard","\nKariuki","\nAdrian"])
content = file.read()
print(content)