gender = input("Enter your Gender(M/F): ")
Salary = eval(input("Enter your Salary: "))
if gender == "M":
    if Salary > 1000:
        print("Your Salary is ", Salary * 1.1)
    else :
        print("Your Salary is ", Salary * 1.5)
elif gender == "F":
    print("Your Salary is ", Salary * 1.2)