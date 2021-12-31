class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
    
    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def talk(self):
        print('{} is talking'.format(self.first_name))

    def get_last_name(self):
        print("{}\'s last name is {}".format(self.first_name, self.last_name))


jack = Person('Jack', 'Harlow', 26)
yeah = hasattr(jack,"first_name")
yeah2 = getattr(jack, "nope", 500)

print(type(jack))

        
