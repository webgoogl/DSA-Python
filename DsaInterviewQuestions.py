""" -------------------------------------------------------------------------"""
""" -------------------------------------------------------------------------"""

# Merge two diff array in sorted form


a=[2,100,200,-1]
b=[3,10,12]
c=a+b

for i in range(len(c)):
    for j in range(len(c)):
        if c[i]<=c[j]:
            tem=c[i]
            c[i]=c[j]
            c[j]=tem
print("Sorted Array -> ",c)

print("\n")



# Print Reverse Array Without using ReverseMethod with using functions

# | a.sort() -> can sort array in ascending order |
# | sorted(a) -> can also sort array in one line |


a=[2,100,200,-1,3,4,50,6,8,9,10,20,25,-12,45,501]

l=len(a)-1

for i in range(len(a)):
    for j in range(len(a)):
        if a[i]<=a[j]:
            tem=a[i]
            a[i]=a[j]
            a[j]=tem
print(f"Maximum Element in array is {a[l]}")
print(f"Maximum Element in array is {a[0]}")


""" -------------------------------------------------------------------------"""
""" -------------------------------------------------------------------------"""

# Print Reverse Array Without using ReverseMethod

print("\n")

a=[2,3,4,5,6,8,9,10,20]
x=len(a)-1

for i in range(len(a)//2):
    tem=a[i]
    a[i]=a[x]
    a[x]=tem
    x=x-1

print(a)
    
""" -------------------------------------------------------------------------"""
""" -------------------------------------------------------------------------"""
