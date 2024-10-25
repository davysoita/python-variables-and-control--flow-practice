# python program to checj the password entered by the user
def my_password():
    user = input("Enter  password")
    if user =="python123":
        return "Correct password"
    else:
        return "Wrong password"
print(my_password())