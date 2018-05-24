class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        if self.fuel == 1:
            fuel_level = "Full"
        elif self.fuel >= 0.5:
            fuel_level = "Kind of Full"
        elif self.fuel > 0:
            fuel_level = "Not Full"
        else:
            fuel_level = "Empty"
        print("----------------------------")
        print("Price: {}".format(self.price))
        print("Speed: {}mph".format(self.speed))
        print("Fuel: {}".format(fuel_level))
        print("Mileage: {}mpg".format(self.mileage))
        print("Tax: {}".format(self.tax))
        

car1 = Car(2000, 35, 1, 15)
car2 = Car(2000, 5, 0.25, 105)
car3 = Car(2000, 15, 0.75, 95)
car4 = Car(2000, 25, 1, 25)
car5 = Car(2000, 45, 0, 25)
car6 = Car(20000000, 35, 0, 15)