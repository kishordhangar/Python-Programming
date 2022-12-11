#7 Write a Python function to print the largest number of three given values
num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
num3=int(input('Enter third number: '))
def largestnumber(a,b,c):
 if a>b and a>c:
 print(a,'is the largest number of',b,'and',c)
 elif b>c:
 print(b,'is the largest number of',a,'and',c)
 else:
 print(c,'is the largest number of',a,'and',b)
largestnumber(num1,num2,num3)