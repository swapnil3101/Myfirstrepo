class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

# Polymorphism using function
def make_sound(animal):
    animal.sound()

make_sound(Cat())
make_sound(Dog())