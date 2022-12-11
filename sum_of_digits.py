#6 Write a Python function to print sum of digits of number n
num=int(input('Enter any number: '))
def sumofdigits(n):
 s=0
 for i in range(n+1):
 s=s+i
 print(s)

sumofdigits(num)