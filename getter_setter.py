class Employee():
    def __init__(self,name = 'Name:'):
        self.__name = name
    
    @property
    def name(self):
        print(self.__name)

    @name.setter
    def name(self,new_name):
        self.__name = new_name 

    @name.deleter
    def name(self):
        del self.__name
    


e1 = Employee()

e1.name = 'Billy'

del e1.name
e1.name = 'Bob'
e1.name