#12 Write a Python function to check the number is prime or not
num=int(input("Enter any number: "))
def primeornot(n):
    for i in range(2,n):
        if n%i==0:
            print(num,'is not a prime')
            break
        else:
            print(num,'is prime')
primeornot(num)