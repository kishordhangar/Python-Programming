#24 Write a Python function to check whether the given character is vowel or consonant
char=input('Enter any chararcter: ')
def vowelorconso(ch):
    vowel='aeiouAEIOU'
    if ch in vowel:
        print(char,'is a vowel')
    else:
        print(char,'is a consonant')
vowelorconso(char)