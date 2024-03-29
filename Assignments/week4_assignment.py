class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print("My name is",self.name,", I'm ",self.age," years old and my gender is",self.gender) 
        
Benard = Person("Benard Kariuki",24,"Male")  

Benard.introduce()         
        