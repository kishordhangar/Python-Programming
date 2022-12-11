#18 Write a Python to check the marital status, gender and age
marsta=input("Enter marital status(married or single): ").lower()
gen=input("Enter your gender(male or female): ").lower()
age=int(input("Enter your age: "))
if marsta=="married":
    print("You are not allowed to marry again")
elif marsta=="single":
    if gen=="male":
        if age>=21:
            print("Congrates, You are eligible to marry")
        else:
            print("Sorry, You are not eligible to marry")
    elif gen=="female":
        if age>=18:
            print("Congrates, You are eligible to marry")
        else:
            print("Sorry, You are not eligible to marry")
    else:
        print('You entered invalid gender')
else:
    print("You entered invalid marital status")