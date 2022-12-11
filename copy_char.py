#21 Write a Python function to copy a given string into new variable and count how many characters are copied
st=input('Enter any string: ')
def copystring(st):
    c=0
    st1=''
    for i in st:
        st1+=i
        c=c+1
    print(st1)
    print(c)
copystring(st)