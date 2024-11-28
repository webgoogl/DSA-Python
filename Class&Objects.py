# CLASS & OBJECTS

# _init_() is a default constructorand and self is refrence parameter

class A:
    " class and objects " # __doc__ string are defined after class
    age=21

    def fun(self):
        " This is fun() __doc__"
        name=" mr coder "
        print(name)
         
a=A()    
a.fun()
print(a.fun.__doc__)
print(a.__doc__)
    

class Coder:
    
    " Testing constructor "
    def __init__(self,name,age):
        print(name," ",age)

ObjCoder=Coder("Suraj",21)
ObjCoder=Coder("Panku",19)
