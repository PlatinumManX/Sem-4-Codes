from abc import ABC, abstractmethod
class Printer(ABC):
    @abstractmethod
    def print_text(self,text:str):
        pass
class IBM(Printer):
    def print_text(self,text:str):
        print("IBM Printer: {}".format(text))
class HP(Printer):
    def print_text(self,text:str):
        print("HP Printer: {}".format(text))
choice=int(input('''1.IBM
2.HP
Enter Your Choice: '''))
if choice==1:
    ibm=IBM()
    text=input("Enter the text to be printed: ")
    ibm.print_text(text)
elif choice==2:
    hp=HP()
    text=input("Enter the text to be printed: ")
    hp.print_text(text)
else:
    print("Invalid Input")
