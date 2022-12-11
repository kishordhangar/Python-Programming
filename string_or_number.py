#24 Write a Python function to check whether user given string or number
x=input('Enter eaither string or number: ')
def strornum(m):
    if m.isalpha()==True:
        print(x,'is a string value')
    elif m.isnumeric()==True:
        print(x,'is a number value')
    elif m.isalnum()==True:
        print(x,'is alpha-numeric value')
    else:
        print(x,'is not a complete string or number or alpha-numeric value')
strornum(x)