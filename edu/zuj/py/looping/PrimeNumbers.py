Prime = True
x= eval(input("Enter a number: "))
for i in range(2,x):
    if x % i == 0:
        print ("Not a prime number")
        Prime = False
        break
if Prime == True:
    print ("Prime number")