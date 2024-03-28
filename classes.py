"""
In Python, a class ia a blue print of an object. A class has got attributes, constructer,
instance attribute and a method. A class method is afunction that is inside the
class.
A constructor is defined using __init__ and self as the first parameter i.e.
def __init__(self) 
A method must also have self as the first parameter.
"""
class Person:
 nationality = "Kenyan"  #class attribute 
 def __init__(self,name,age): #class constructor
   self.name = name #instance attribute
   self.age = age

 def displayinfo(self): #Class method
  print("Person's name is",self.name,"and he is aged",self.age)    
   
     
P1 = Person("Bena", 20)

P1.displayinfo()
