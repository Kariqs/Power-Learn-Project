class Vehicle:
  def __init__(self,color,wheels,engine):
      self.color = color
      self. wheels =wheels
      self.engine = engine
    

class Mazda(Vehicle):
    def __init__(self, color, wheels, engine,model,fuel):
       super().__init__(color, wheels, engine)
       self.model = model
       self.fuel = fuel
       
    def printCar(self):
        print(self.color,self.wheels,self.engine,self.model,self.fuel)
             
       
Car = Mazda("White",4,"V6","Mazda CX-5","Diesel")
Car.printCar()

print(issubclass(Mazda,Vehicle))
 