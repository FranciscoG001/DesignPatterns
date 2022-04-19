
from abc import abstractstaticmethod, ABCMeta

#Abstract base classes cannot be instantiated
class Person(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data():
        """ implement in child class """

class PersonSingleton(Person):

    ## __ for private
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default", 0)
        return PersonSingleton.__instance

    # The __init__ function is called every time an object is created from a class.
    # The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.
    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
    
    #A static method doesn't receive any reference argument whether it is 
    # called by an instance of a class or by the class itself.
    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")
    
p = PersonSingleton("Francisco", 18)
#print(p)
p.print_data()

p1 = PersonSingleton.get_instance()
#print(p1)
p1.print_data()

#Fail
p2 = PersonSingleton("Xico", 20)
p2.print_data()