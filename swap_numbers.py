#11 Write a Python function to swap the given two numbers
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
def swap(x,y):
    temp=x
    x=y
    y=temp
    print('first number is',num1,', after swaping',x)
    print('second number is',num2,', after swaping',y)
swap(num1,num2)