#10 Write a Python function to print factorial of given number
num=int(input('Enter any number: '))
def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    print(s)
factorial(num)