#create an empty list called my_list
my_list = []

#append the following values to my_list: 10,20,30,40
my_list_values = (10,20,30,40)

for value in my_list_values:
 my_list.append(value)
 
#Insert the value 15 at the second position in the list.
my_list[1]=15 

#Extend my_list with another list: [50, 60, 70].
second_list = [50,60,70]
my_list.extend(second_list)

#Remove the last element from my_list.
my_list.remove(70)

#Sort my_list in ascending order.
my_list.sort()

#Find and print the index of the value 30 in my_list.
print("The index of 30 is",my_list.index(30))

#print the list
print(my_list)





