#3 Write a python function to check the given number is divisible by 10 or not?
num=int(input("Enter any number: "))
def divby10(n):
 if n%10==0:
 print(num,'is divisible by 10')
 else:
 print(num,'is not divisible by 10')
divby10(num)