#28 write a Python function to print the following pattern
 #*
 #* *
 #* * *
 #* * * *
 #* * * * *
n=4
def pattern4(n):
    m=8
    for i in range(n+1):
        for j in range(m):
            print(end=' ')
        m=m-2
        for k in range(i+1):
              print('* ',end='')
        print()
pattern4(n)
