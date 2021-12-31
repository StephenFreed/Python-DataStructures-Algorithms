class Animal:
    def __init__(self,name):
        self.name = name
    def noise(self):
        print('{} does animal noises'.format(self.name))

class Lion(Animal):
    def noise(self):
        print('{} goes roooaarrrr'.format(self.name))

class Cat(Animal):
    def noise(self):
        print('{} going prrrrrr'.format(self.name))

class Person:
    def noise(self):
        print('Person does this.')

an_animal = Animal('Animal')
my_lion = Lion('Badass Lion')
my_cat = Cat("Kitty")
my_person = Person()
yeah = [an_animal,my_lion,my_cat,my_person]

for elm in yeah:
    elm.noise()

my_person.noise()

