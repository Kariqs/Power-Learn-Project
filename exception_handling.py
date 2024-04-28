try: #try clause (try... except...)
    name = input("Enter user name:")
    age = int(input("Enter age:"))
    if age<25:
        raise ValueError ("Age must be greater than 25") #raising an exception
except:
    print("An error occured") 
else: # The else clause carries the code that should be executed if there wa no exception
   print("Name:",name,"\nAge:",age)        