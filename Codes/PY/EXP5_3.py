class Car:
    def __init__(self,name,horsepower):
        self.name=name
        self.horsepower=horsepower
    def __gt__(self,other):
        if not isinstance(other,Car):
            return NotImplemented
        return self.horsepower>other.horsepower
    def __str__(self):
        return "{} Hp {}".format(self.horsepower,self.name)
car1_name=input("Enter Name of 1st Car: ")
car1_power=int(input("Enter Horsepower of 1st Car: "))
car2_name=input("Enter Name of 2nd Car: ")
car2_power=int(input("Enter Horsepower of 2nd Car: "))
car1=Car(car1_name,car1_power)
car2=Car(car2_name,car2_power)
if car1>car2:
    print("{} is more Powerful than {}".format(car1,car2))
else:
    print("{} is less Powerful than {}".format(car1,car2))
