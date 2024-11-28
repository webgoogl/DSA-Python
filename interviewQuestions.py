# BYTECODE - is a low level converted code by compiler and not human readable after converting into byte code interpereter intreted it line by line

# GLOBLE VARIABLE are public varible define in globle scope. GLoble variables are used inside function through globle keyword

# PROTECTED attributes are marked with _a single underscore . While they can still be accessed and modified from outside of class , responsible
# developers should avoid doing this.

# PRIVATE attribute are marked with double underscore __good .These cant be accessed or modified directly from outside the class and any such
# attempted this AttributeError

# To remove file through python [os.remove()/os.unlink()]

# Python sort()/ sorted() function use tim sort algorithm to perform sorting over data . Tim sort algorithm is hybrid algorithm made up of merge sort and
# insertion sort worst-case is | O( nlogn ) |


##########################################################################################################################################################
"""----------------------------------------------------------------------------------------------------------------------------------------------------"""

import pandas as pd

data = {
    "s.no" : "a",
    "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 

"""----------------------------------------------------------------------------------------------------------------------------------------------------"""
##########################################################################################################################################################

#Capitalize()
name="suraj"
print(name.capitalize())


#Generator()
def function_name():
    yield "suraj"
    yield 20
    yield "panku"

x=function_name()
for i in x:
    print(i)

"""----------------------------------------------------------------------------------------------------------------------------------------------------"""

# docstrings()

def functions(n):
    ''' Takes n positional argument '''
    print(n*2)

functions(5)
print(functions.__doc__)
print("\n")

# SHALLOW COPY   AND    DEEP COPY
# | copy.copy()/copy()/list.copy() || copy.deepcopy()

""" In Deepcopy we have to import copy first then use """

import copy

list1=[2,3,[4,5]]
      # list2=list1.copy()

list2=copy.deepcopy(list1)
      # list2=copy.copy(list1)
list1[-1][-1]=123

print(list1)
print(list2)

print("\n")

# *args || **kwargs

def additions(*nums,**num):
    # *nums give data in tuple form 
    # **num give data in dictionry form

    
    print(sum(num.values()))
    print("\n")
    
print(additions(2,3,4,5,n1=2,n2=4))


# zip() Function

a=("suraj","pankaj")
b=("ayush","harsh")
x=zip(a,b)
print(tuple(x))

print("\n")

# Fibonacci series


a=0
b=1
k=int(input(" Enter a range : "))
for i in range(k):
    print(a,end=" ")
    c=a+b
    a=b
    b=c 
print("\n")

# Fibonacci series through function 
def fibonacci(n):
    l=[0,1]

    while len(l)< n:
        l.append(l[-1]+l[-2])
    return l

n=int(input("Enter range of fibonacci : "))
print(f"Fibonacci series of {n} terms -- ")
print(fibonacci(n)) 

"""----------------------------------------------------------------------------------------------------------------------------------------------------"""






    
    
    
