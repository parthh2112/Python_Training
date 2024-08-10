
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


#Multiple Inheritance
class Flying:
    def fly(self):
        return f"{self.name} can fly."
    
class Swimming:
    def swim(self):
        return f"{self.name} can swim."

class Duck(Flying, Swimming):
    def __init__(self, name):
        self.name = name

#Multilevel

class Vehicle:
    def __init__(self, name):
        self.name = name

    def start(self):
        return f"{self.name} starting..."

class Car(Vehicle):
    def drive(self):
        return f"{self.name} driving..."

class ElectricCar(Car):
    def charge(self):
        return f"{self.name} charging..."
    


def main():
    dog = Dog("Mike")
    print(dog.speak())

    duck = Duck("Donald")
    print(duck.fly())
    print(duck.swim())

    car = ElectricCar("Tesla")
    print(car.start())
    print(car.drive())
    print(car.charge())

if __name__ == "__main__":
    main()



