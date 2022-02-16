# ~~~~~~~~~~ Protected Access Modifier ~~~~~~~~~~

# one _ before variable or method signifies protected access

class Person:

    name = None
    age = None
    # protected instance variable
    _social_security = None

    # constructor
    def __init__(self, name, age, social_security):
        self.name = name
        self.age = age
        self._social_security = social_security

    # protected should have getters and setters
    def set_social_security(self, social_security):
        self._social_security = social_security

    def get_social_security(self):
        return self._social_security


stephen = Person("Stephen", 36, 12345)
print(stephen.name)
print(stephen.age)
print(stephen._social_security)  # still able to access protected attribute
stephen.set_social_security(9999999)  # setting new social
print(stephen.get_social_security())  # getting social


# ~~~~~~~~~~ Private Access Modifier ~~~~~~~~~~

# two __ before variable or method signifies private access


class PrivatePerson:

    name = None
    age = None
    # private instance variable
    __social_security = None

    # constructor
    def __init__(self, name, age, social_security):
        self.name = name
        self.age = age
        self.__social_security = social_security

    # private must have getters and setters
    def set_social_security(self, social_security):
        self.__social_security = social_security

    def get_social_security(self):
        return self.__social_security


stephen = PrivatePerson("Stephen", 36, 12345)
print(stephen.name)
print(stephen.age)
# print(stephen.__social_security)  # trying to access private attribute throws error
stephen.set_social_security(9999999)  # setting new social
print(stephen.get_social_security())  # getting social
