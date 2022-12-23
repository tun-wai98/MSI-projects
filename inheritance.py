class Vehicle():
#parent class coz ()
#init method is also called constructor which is worked first when object is created.
#other method is print hello method. It prints hello.
 #init method needs parameter such as color.
    def __init__(self,color):
        self.color = color
    def print_hello(self):
        print('Hello')

#car class is the child class of vehicle class.
#class Car(Vehicle):
    #pass

#method overriding
class Car(Vehicle):
    def print_hello(self):
        print('Not hello')

#method adding
     


#super fuction
#parent class methods and variables are called.

#multiheritance



#pass is written when we dont want to write and error.
car1 = Car('BMW')
print(car1.color)
#car class dont own init method but it has. coz parent class has init method,
#we cant print color coz private method. So we need to use self and get method.
car1.print_hello()

    
