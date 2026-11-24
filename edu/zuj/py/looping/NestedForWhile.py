while True:
    x= eval(input("Enter a number (Negative Number to Stop): "))
    if x < 0:
        break
    for i in range (2,x):
        if x % i == 0:
            print (x, "is Not Prime.")
            break
    else:
            print (x, "is Prime.")