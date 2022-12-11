#16 Write a Python function to print first 10 fibonacci series numbers
num=int(input('Enter any number: '))
def fibonacci1(n):
    t1=0
    t2=1
    lst=[0]
    temp=0
    while temp<10000:
        temp=t1+t2
        t1=t2
        t2=temp
        lst.append(t1)
        if len(lst)==n:
            break
    for i in lst:
        print(i)
fibonacci1(num)