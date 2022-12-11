#20 Write a Python function to remove vowels from given string
st=input('Enter any string :')
v='aieouAEIOU'
st=list(st)
for i in st:
    if i in v:
        st=st.replace(i,'')
    st=''.join(st)
print(st)