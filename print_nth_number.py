#19 Write a Python function to print nth table
num=int(input("Enter any number: "))
def tabledisplay(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
tabledisplay(num)