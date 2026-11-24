grade =eval(input("Enter your grade: "))
if 0 < grade < 60:
    print("Your grade is F")
elif 70 > grade > 60:
    print("Your grade is D")
elif 80 > grade > 70 :
    print("Your grade is C")
elif 90 > grade > 80 :
    print("Your grade is B")
elif 99 > grade > 90 :
    print("Your grade is A")
elif grade == 100 :
    print("Your grade is A+")
else:
    print("Invalid Grade.")