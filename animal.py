class Animal(object):
    def __init__(self, name = None, health = None):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print (self.health)
        return self

class Dog(Animal):
    def __init__(self, name, health = 150):
        Animal.__init__(self, name, health)
    
    def pet(self):
        self.health += 5
        return self
    
class Dragon(Animal):
    def __init__(self, name, health = 170):
        Animal.__init__(self, name, health)
    
    def fly(self):
        self.health -= 10
        return self
    
    def display_health(self):
        Animal.display_health(self)
        print ("I am a Dragon")
        return self

animal = Animal("Bill", 400)
dog = Dog("Rex")
dragon = Dragon("Bud")

dog.walk().walk().walk().run().run().pet().display_health()

dragon.fly().fly().display_health()