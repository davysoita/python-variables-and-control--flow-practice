# python program to check if a number entered by user is odd or even
def myNumber():
    number = int(input("Enter a number: "))
    if number %2 == 0:
        print ("This is an even number")

    else:
        print("This is an odd numer")
    return number