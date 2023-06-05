"""Classes and Decorators"""
from abc import ABC, abstractmethod


class Human(ABC):
    __id = 1

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__id = Human.__id
        Human.__id += 1

    @abstractmethod
    def __repr__(self):
        return 'I am human'

    def __add__(self, other):
        return f'{self.__name} and {other.__name} hung out'

    def __sub__(self, other):
        return f'{self.__name} parted ways with {other.__name}'

    def __del__(self):
        del self

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        print(f'{self.__name} has changed their name to {new_name}')
        self.__name = new_name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, increment):
        self.__age += increment
        print(f'Happy Birthday {self.__name}! You are now {self.__age}!')

    @age.deleter
    def age(self):
        del self.__age

    def communicate(self):
        print(f'Hi, my name is {self.__name}, and I\'m {self.__age} years old')


class Male(Human):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __repr__(self):
        return 'I am a male'


class Female(Human):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __repr__(self):
        return 'I am a female'


sofia = Female('Sofia', 26)
diego = Male('Diego', 30)

print(diego)
date = sofia + diego
end_date = sofia - diego
print(date)
diego.communicate()
sofia.communicate()
print(end_date)
        
