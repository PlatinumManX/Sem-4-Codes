class Salary:
    def __init__(self, basic, hra, pf):
        self.basic=basic
        self.hra=hra
        self.pf=pf
        self.net_salary=self.calculate()
    def calculate(self):
        return self.basic+self.hra-self.pf
    def display(self):
        return "Basic: {}\nHRA: {}\nPF: {}\nNet Salary: {}".format(self.basic,self.hra, self.pf, self.net_salary)
    
