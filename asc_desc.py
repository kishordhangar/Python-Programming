#17 Write a Python function to print the given three values in asc and desc order
a=eval(input("Enter first value: "))
b=eval(input("Enter second value: "))
c=eval(input("Enter third value: "))
def orderofvalues(x,y,z):
    if x>y and x>z:
        if y>z:
            print('the desc order is ',x,y,z)
            print('the asc order is',z,y,x)
        else:
            print('the desc order is ',x,z,y)
            print('the asc order is ',y,z,x)
    elif y>x and y>z:
        if x>z:
            print('the desc order is ',y,x,z)
            print('the asc order is ',z,x,y)
        else:
            print('the desc order is ',y,z,x)
            print('the asc order is',x,z,y)
    elif z>x and z>y:
        if x>y:
            print('the desc order is ',z,x,y)
            print('the asc order is ',y,x,z)
        else:
            print('the desc order is ',z,y,x)
            print('the asc order is ',x,y,z)
orderofvalues(a,b,c)