def age_checker():
    age = int(input("enter your age: "))
    if age <0:
        return "Age can not be negative"
    if age < 18:
        return "You are a minor"
    elif age <= 65:
        return "You aare an adult"

    else:
        return "You are a senior"
print(age_checker())