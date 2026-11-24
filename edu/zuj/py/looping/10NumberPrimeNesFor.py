for j in range(10):
    x= eval(input("Enter a number: "))
    for i in range (2, x):
        if x % i == 0:
            print (x, "Is not Prime.")
            break
    else:
        print (x, "Is Prime.")