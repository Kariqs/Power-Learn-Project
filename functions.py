# def add_numbers(a,b):
#     results =  a+b
#     print("The sum is: ",results)

# sum = add_numbers(3,4) 

#a lambda function
print_name = lambda name: print(name) 

def print_names():
    names=[]
    for i in range(3):  
     name = input("Enter a name: ")  
     names.append(name)
    for nam in names:
        print(nam)   
        
def is_even(a):
    if a%2 == 1:
        return False
    else:
        return True   
    
                 

#use args
def print_nums(*num):
    print(num)

print_nums(1,2,3,4,5,6)    

#use kwargs
def print_ages(**ages):
    for k,v in ages.items():
        print(v)

print_ages(Benard=22,Jean=30)        

print_names()

is_even(4)

print_name("Bena")