class Profile:
     def __init__(self, name, age, dob):
         self.name=name
         self.age=age
         self.dob=dob
     def display(self):
         return "Name: {}\nAge: {}\nDOB: {}".format(self.name, self.age, self.dob)
        
