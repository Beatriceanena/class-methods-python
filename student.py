class Student:
    school="Akirachix"
    def __init__(self,first_name,last_name,age,country,year_of_birth):
         self.first_name=first_name
         self.last_name=last_name
         self.age=age
         self.country=country
         self.year_of_birth=year_of_birth
    

     
    def greet(self):
        return f"Hello {self.name},  welcome to {self.school} How is {self.country}"
    def full_name(self):
        return f"Hello my name is {self.first_name} {self.last_name}"
    def year_of_birth(self):
        return 2000-self.age    
    def initials(self):
        return f"Your initials are {self.first_name[0]} {self.last_name[0]}"
    
