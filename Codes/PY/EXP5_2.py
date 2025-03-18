class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def vehicle_info(self):
        return "Brand: {}\nModel: {}".format(self.brand,self.model)
class Engine:
    def __init__(self,engtype,horsepower):
        self.engtype=engtype
        self.horsepower=horsepower
    def engine_info(self):
        return "Engine Type: {}\nHorsepower: {}".format(self.engtype,self.horsepower)
class Car(Vehicle, Engine):
    def __init__(self,brand,model,engtype,horsepower,color):
        Vehicle.__init__(self,brand,model)
        Engine.__init__(self,engtype,horsepower)
        self.color=color
    def car_info(self):
        return "{}\n{}\nColor: {}".format(self.vehicle_info(),self.engine_info(),self.color)  
brand=input("Enter the Brand of the car: ")
model=input("Enter the Model of the car: ")
engtype=input("Enter the Engine type of the car: ")
horsepower=int(input("Enter the Horsepower of the car: "))
color=input("Enter the Color of the car: ")
obj=Car(brand,model,engtype,horsepower,color)
print("\nCar Information:-")
print(obj.car_info())
