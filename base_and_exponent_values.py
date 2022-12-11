#23 Write a Python function to print power values based on two given base and exponent values
base=int(input('Enter base value: '))
expo=int(input('Enter exponent value: '))
def power(m,n):
    x=base**expo
    print(x)
power(base,expo)