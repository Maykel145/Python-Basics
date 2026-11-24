Sum = 0
Count = 0
while True:
    Grade = eval(input("Enter your grade (Negative Number to Stop): "))
    if Grade < 0:
        break
    Sum = Sum + Grade
    Count = Count + 1
if Count > 0:
    print ("Your Grade is: ", Sum / Count)
else:
    print ("No Grades Where Entered.")