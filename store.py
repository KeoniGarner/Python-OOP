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

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    
    def add_product(self, product):
        self.products.append(product)
        return self
    
    def remove_product(self, product_name):
        for product in self.products:
            if product.item_name == product_name:
                self.products.remove(product)
        return self
    
    def inventory(self):
        if self.products == []:
            print ("There are no items in the store!")
        for product in self.products:
            product.display_info()
            print ("----------")
        return self

product1 = Product(200, "Shirt", 5, "Supreme")
store = Store([], 1, "Frank")
store.add_product(product1).inventory().remove_product("Shirt").inventory()