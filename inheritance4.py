class Person: # Parent class / Base
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def introduce(self):
        print(f"Hello my name is {self.firstname} {self.lastname}.")
        
class Student(Person): # Child
    def __init__(self,firstname,lastname,sectionYear):
        super().__init__(firstname,lastname)
        self.sectionYear = sectionYear
        
    def introduce(self):
        print(f'My name is {self.firstname} {self.lastname} from {self.sectionYear}')
print('Parent full-name:')  
personOne = Person('Elon','Musk')
personOne.introduce()
print('Student info:')
studentOne = Student('Louwis Alfred','Nabayan','SBIT3B')
studentOne.introduce()   
 
      
"""
firstname = input('Enter firstname: ').strip().capitalize()
lastname = input('Enter lastname: ').strip().capitalize()
personOne = Person(firstname,lastname)
personOne.introduce()

print('Enter student details')
firstname = input('Enter firstname: ')
lastname = input('Enter lastname: ')
sectionYear = input('Enter Section / Year: ')
studentOne = Student(firstname,lastname,sectionYear)
studentOne.introduce()
"""