
#26 Write a Python function to print the following pattern

n=4
def pattern2(n):
    for i in range(n+1):
        for j in range(i):
            print('*',end=' ')
        print('\n')
pattern2(n)
