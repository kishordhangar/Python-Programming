#2 Write a python function to check the given number is positive or negative
num=int(input("Enter any value: "))
def posornegorzero(n):
 if n>0:
 print(num,'is positive number')
 elif n==0:
 print('the given number is',num)
 else:
 print(num,'is negative number')
posornegorzero(num)