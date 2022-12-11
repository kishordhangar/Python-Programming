#14 check gven number is armstrong or not
num=int(input('Enter any three digit number: '))
def armstrongornot(n):
    s=0
    while n>0:
        digit=n%10
        s+=digit**3
        n//=10
    if num==s:
        print(num,'is a armstrong number')
    else:
        print(num,'is not a armstrong number')
armstrongornot(num)