#15 print fibonacci series for below n number
num=int(input("Enter any number: "))
def fibonacci(n):
    t1=0
    t2=1
    for i in range(10000):
        temp=t1+t2
        t1=t2
        t2=temp
        if t1>=n:
            break
        print(t1)
fibonacci(num)