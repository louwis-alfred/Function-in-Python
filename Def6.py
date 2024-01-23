class Fruit:
    def __init__(self,name,vitamin):
        self.name = name
        self.vitamin = vitamin
        
    def vitamins(self):
        print(f'This {self.name} is rich in {self.vitamin}')


# Create an instance of the Fruit Class
fruit_instance = Fruit(name='',vitamin='')

# Get user input       
name = input('Enter fruit: ')
vitamin = input('Enter vitamin: ')
       
# Set the values for the instance
fruit_instance.name = name
fruit_instance.vitamin = vitamin

# Call the vitamins method on the instance 
fruit_instance.vitamins()
