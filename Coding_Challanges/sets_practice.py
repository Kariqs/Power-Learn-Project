"""
1. Write a program that accepts user input to create a list of integers. 
Then, compute the sum of all the integers in the list.
"""

#take user input of the length of the list.
range_value = int(input("Enter a range of integers you want to sum:"))
integers = []

for _ in range(range_value):
 integer = int(input("Enter an integer:"))#convert user input to an integer.
 integers.append(integer)#add user input to the integers list.
sum = sum(integers) 
print(sum)


"""
2. Create a tuple containing the names of five of your favorite books.
Then, use a for loop to print each book name on a separate line.
"""
favourite_books = ("The Rational Male.","Think and Grow Rich.","Rich Dad Poor Dad.","The Unplugged Alpha.","The Way of the Superior Man.")
for book in favourite_books:
    print(book)

"""    
3. Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. 
Then, print the dictionary to the console.    
"""
person = {}
name = input("Enter your name:")
person["name"] = name
age =int(input("Enter you age:"))
person["age"]=age
color = input("Enter your favourite color:")
person["favourite_color"]=color
print(person)

"""
4. Write a program that accepts user input to create two sets of integers. 
Then, create a new set that contains only the elements that are common to both sets.
"""
names = set()
numbers = set()

for _ in  range(3):
    name = input("Enter a name: ")
    names.add(name)
print(names)

for _ in range(4):
    num = int(input("Enter a number: "))
    numbers.add(num)
print(numbers)

print("The common values are: ",names.intersection(numbers))

"""
Create a program that stores a list of words. 
Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
"""
words = ["Good","name","two","five","sixteen"]
for word in words:
    if len(word)%2==1:
        print(word)