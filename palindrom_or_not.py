#13 Write a Python function to check the given number is palindrom or not
n=input("Enter any number: ")
def palindromeornot(num):
    if num==str(num)[::-1]:
        print(num,'palindrome number')
    else:
        print(num,'not a palindrome number')
palindromeornot(n)