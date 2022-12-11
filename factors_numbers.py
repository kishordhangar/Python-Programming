#9 Write a Python function to print the factors of given number
num=int(input('Enter any value: '))
def factors(n):
 for i in range(1,n+1):
 if n%i==0:
 print(i)
factors(num)