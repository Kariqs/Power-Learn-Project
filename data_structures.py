name = ["Irene","Benard","Adrian","Edel"]
name[0]="Allan" #change the value of the first element of the list.
print(name) #prints the list of names
print(name[0])#prints the first element of name
print(name[0:3])#prints the first to the third element of a list.This is called slicing
print(name[-1]) # This prints the last element of a list. Therefore, -2 will print the second last element and so on.

"""
A list can have different or one data type.
You can have a list of only strings or only integers.
You can also have a list of more than one data type. You can have a list with combined integers and strings.
e.g. combined = ["Benard",39,12+j]
A list is a mutable data structure and therefore can be modified.
"""
name.append("Kariuki")#add a value to the name list.
print(name)
numbers=[1,2,3,4,5,6]#Create a list of numbers.
name.extend(numbers)#add the values of numbers to name

#to delete an element from a list, we use the del keyword followed by the element
del_name = ["A","B","C"]
del del_name[0] # deletes the first element of del_name.
print (del_name)

#iterating through a list can also be done.
for a_name in name:
    print(a_name)
    #The above prints individual element from a list.


#TUPLES
names = ("Ben","Chen","Dan","Ken")
print(names[0])