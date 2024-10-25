# python program to day of the Week
def day_of_the_week(day):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(int(day), "invalid day")
print(day_of_the_week(2))