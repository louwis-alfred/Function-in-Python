class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price:,.2f}")
        
carOne = Car('Tesla','X',50000)
carOne.details()
