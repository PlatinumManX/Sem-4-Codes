class Customer:
    def __init__(self, id, name, mobile):
        self.id=id
        self.name=name
        self.mobile=mobile
    def __str__(self):
        return "{}, {}, {}".format(self.id, self.name, self.mobile)

def save(filename, customers):
    with open(filename, "w") as file:
        for customer in customers:
            file.write(str(customer)+"\n")
    print("\nCustomer Details saved to {}".format(filename))

def read(filename):
    print("\nReading Customer Details from {}\n".format(filename))
    with open(filename, "r") as file:
        content=file.readlines()
        i=1
        for line in content:
            id, name, mobile=line.strip().split(",")
            print("{}) ID: {}, Name:{}, Mobile: {}".format(i, id, name, mobile))
            i=i+1

filename="customers.txt"
customers=[]
n=int(input("Enter the Number of Customers: "))
for i in range(n):
    print("Enter Details of Customer {}:-".format(i+1))
    id=int(input("Enter the ID: "))
    name=input("Enter Name: ")
    mobile=int(input("Enter the Mobile Number: "))
    customers.append(Customer(id, name, mobile))
save(filename, customers)
read(filename)
