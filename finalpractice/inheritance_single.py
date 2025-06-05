class Animal:
    def speak(self):
        print("I am an animal")

class Dog(Animal):
    def speak(self):
        print("I bark")

# Using inheritance
a = Animal()
a.speak()

d = Dog()
d.speak()