# Parent class
class Person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    def introduce(self):
        print(f'My name is {self.firstName} {self.lastName}.')  
        
# Child class
class Student(Person):
    def __init__(self,firstName,lastName,sectionYear):
        super().__init__(firstName,lastName)
        self.sectionYear = sectionYear
        
    def introduce(self):
        print(f"Hi i am {self.firstName} {self.lastName} from {self.sectionYear}.")
        # super().introduce()
        
class Employee(Person):
    def __init__(self, firstName, lastName,position):
        super().__init__(firstName,lastName)
        self.position = position
        
    def introduce(self):
        print(f"My name is {self.firstName} {self.lastName} and my position is {self.position}")

        

        
