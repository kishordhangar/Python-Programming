#29 Write a Python function print the following pattern
#'''
#* * * * *
#* * * *
#* * *
#* *
#*
#Python Programs
n=5
def pattern5(n):
 for i in range(n+1):
 for j in range(1,(n-i)+1):
 print('*',end=' ')
 print()

pattern5(n)
 