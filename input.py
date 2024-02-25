#the code in this file takes user name from a user and adds it to a list.
names = []

while len(names)<9:
 name = input("Enter your name:")
 names.append(name)

print(names)