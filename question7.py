# python program to check the type of the triangle
def triangle():
    j = int(input("Enter j: "))
    h = int(input("Enter h: "))
    k = int(input("Enter k: "))
    if j <= 0 or h <= 0 or k <= 0:
        return "Sides must be positive"
    if j == h == k:
        return "Equilateral triangle"
    elif j == h or j == k or h == k:
        return "Isosceles triangle"
    else:
        return "Scale triangle"
print(triangle())