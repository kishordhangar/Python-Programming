#25 Write a Python function to print the follwing pattern
#****
#****
#****
#****
n=4
def pattern1(n):
    for i in range(n):
        for j in range(n):
            print('*',end=' ')
        print('\n')
pattern1(n)