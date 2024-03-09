names = []
name_i_want = "Benard"
for i in range(3):
    name= input("Enter your name:")
    names.append(name)
    for nam in names:
        if nam == name_i_want:
         print(nam)
        else:
            print("This is not the name I am looking for.") 
         
#list comprehension
numbers = [1,2,3,4,5]
doubled = [num*2 for num in numbers]
print(doubled)         