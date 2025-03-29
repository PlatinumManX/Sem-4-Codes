class Qualification:
    def __init__(self, degree, experience):
        self.degree=degree
        self.experience=experience
    def display(self):
        return "Degree: {}\nExperience: {} years".format(self.degree, self.experience)
