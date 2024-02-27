#Dictionaries are created using a key and a value all put in curly braces.
#Compared to JavaScript, dictionaries are like objects only that the value and the key can sometimes be strings.
"""
Keys and values can all be strings or all integers or a string and an integer.
"""
capital_city = {"Kenya":"Nairobi","Uganda":"Kampala"} #both key and value are strings
capital_city["Japan"]="Tokyo" #adding an element to a dictionary.
print(capital_city["Kenya"])
print(capital_city.keys())

numbers={1:"One",2:"two"}
print(numbers)
del numbers[1] #delete an element from a dictionary.
print(numbers)

squares = {1:1,3:9,4:16,5:25}
#the code below tests for membership in a dictionary.
#when checking for membership, we use the key then in keyword to check if the key belongs to the dictionary.
print (1 in squares) #returns true.
print (3 not in squares)#returns false.

#iterating through a dictionary

for sq in squares:
    print(sq)