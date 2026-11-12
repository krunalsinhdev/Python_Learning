# Single Inheritance
# A child class can reuse methods and attributes from a parent class.

class Animal:
    def eat(self):
        print("This animal eats food.")

class Dog(Animal):
    def bark(self):
        print("The dog barks.")

dog = Dog()
dog.eat()   # Inherited method
dog.bark()
