class Product(object):
    def __init__(self, price, item_name, weight, brand, status="For Sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        self.status = "Sold!"
        return self
    
    def add_tax(self, tax):
        return self.price * (1 + tax)
    
    def return_item(self, reason):
        if reason == "defective":
            self.status = "Defective"
            self.price = 0
        
        if reason == "new":
            self.status = "For Sale"

        if reason == "used":
            self.status = "Used"
            self.price *= 0.8
        
        return self
    
    def display_info(self):
        print("Product Name: {}".format(self.item_name))
        print("Price: ${}".format(self.price))
        print("Weight: {}lbs".format(self.weight))
        print("Brand: {}".format(self.brand))
        print("Status: {}".format(self.status))
        return self

product = Product(200, "Shirt", 5, "Supreme")
print(product.add_tax(0.075))
product.return_item("new").display_info()
product.return_item("used").display_info()
product.return_item("defective").display_info()