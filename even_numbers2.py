#4 Write a Python function to print first n even numbers
num=int(input('Enter any number: '))
lst=[]
def nevennums(n):
 for i in range(10000):
 if i%2==0:
 lst.append(i)
 if len(lst)==n:
 break
 print(lst)

nevennums(num)