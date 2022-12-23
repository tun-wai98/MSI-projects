#creating a class
from turtle import pencolor


class Car:
    def __init__(self, color, year, model):
        self.__color = color
        self.__year = year
        self.__model = model

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def selfModel(self,model):
        self.__model = model 

    def getModel(self):
        return self.__model 
#def is function but def under class is method.
#self.color is variable & pcolor is parameter.
#attribute is variable.
    no_of_wheel = 4
#no_of_wheel which is outside of init(method) = class attribute or class level variable. 
#Self.color which is inside the init(method) is instant attribute or class attribute.

#creating object
car1 = Car('Yellow', 2010, 'BMW')
#car1 is object name of car class. We need to input parameters because init method asks them.

#print(car1.color)
#print(car1.model)
#print(car1.year)
#print(car1.no_of_wheel)

car1.year = 'brown'
print(car1.year) 

car1.setColor('blue')
print(car1.getColor())

car1.selfModel('Toyota')
print(car1.getModel())
# year brown is inconvinent. So we need to use data hiding(encapsulation). 
# Encapsulation prevents data changing by others. 
# double underscoring --->  after data hide, varibale cant be seen by others. It errors.
# for other language, we input private before variable.
# the four pillors of OOP concept are encapsulation, inheritance, abstract, polymorphism.

