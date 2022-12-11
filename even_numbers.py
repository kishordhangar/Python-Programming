#5 Write a Python function to print even numbers upto n
num=int(input('Enter any number: '))
def firstnevennums(n):
 for i in range(n+1):
 if i%2==0:
 print(i)
firstnevennums(num)