class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def display_info(self):
        print("Price: {}".format(self.price))
        print("Max Speed: {}".format(self.max_speed))
        print("Miles: {}".format(self.miles))
        return self

    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    
    def reverse(self):
        print("Reversing")
        if (self.miles - 5 >= 0):
            self.miles -= 5
        else:
            self.miles = 0
        return self

bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().display_info()

bike2 = Bike(500, "10mph")
bike2.ride().ride().reverse().reverse().display_info()

bike3 = Bike(1000, "1mph")
bike3.reverse().reverse().reverse().display_info()