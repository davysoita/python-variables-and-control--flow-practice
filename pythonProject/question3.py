# python program to ward grade based on the input as per the user
def my_grade(mark):
    if mark<0 or mark>100:
        return " Invalied marks, kindly enter valied marks"
    else:
        if mark >=90:
            grade = 'A'
        elif mark >=80:
            grade = 'B'
        elif mark >=70:
            grade = 'C'
        elif mark >=60:
            grade ='D'
        else:
            grade = 'F'
        return grade
print(my_grade(100))