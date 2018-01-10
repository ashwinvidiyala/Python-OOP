class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "{}'s Health: {}".format(self.name, self.health)

animal = Animal('animal', 100)
animal.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)

    def pet(self):
        self.health += 5
        return self

dog = Dog('dog')
dog.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name, health=170):
        self.name = name
        self.health = health

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print "This is a dragon!"

dragon = Dragon('dragon')
dragon.fly().display_health()
