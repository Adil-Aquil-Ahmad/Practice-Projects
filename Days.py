import math
def Day_Check():
    Date = str(input("Input the Date seperated by / :"))
    print(Date)
    Date = Date.replace("/", " ")
    e, f, g = Date.split()
    while True: 
        try: 
            e = int(e)
            f = int(f)
            g = int(g)
            break
        except ValueError: 
            print("Invalid input. Please enter an integer.")
            Day_Check()
    while True: 
        try: 
            month = f 
            if 1 <= month <= 12: 
                break 
            else: 
                print("Input must be between 1 and 12.")
                Day_Check()
                
        except ValueError: 
            print("Invalid input. Please enter an integer.")
            Day_Check()
    while True: 
        try: 
            year = g 
            if 1 <= year <= 2099: 
                break 
            else: 
                print("Input must be between 1 and 2099.")
                Day_Check()
        except ValueError: 
            print("Invalid input. Please enter an integer.")
            Day_Check()
    x = 0
    a = 29
    b = 28
    days = 0
    if (year%4==0 and year%100!=0) or year%400==0:
        x=a
    else:
        x=b
    Dict_days = {0: 'sunday', 1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday', 6: 'saturday'}
    Dict_months = {1: 31, 2: x, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if year%4==0:
        x=a
    else:
        x=b
    print("Calender:", Dict_months)
    while True: 
        try: 
            day = e 
            if 1 <= day <= Dict_months[month]: 
                break 
            else: 
                print("Input must be between 1 and {}.".format(Dict_months[month]))
                Day_Check()
        except ValueError: 
            print("Invalid input. Please enter an integer.")
            Day_Check()


    for i in range(1, month):
        days += Dict_months[i]
    days += day
    days += (year-1)*365
    y = 0
    for j in range(1, year):
        if (j%4==0 and j%100!=0) or j%400==0:
            y+=1
    days += y
    DAY = days%7
    print("No. of leap years from 01/01/2001:",y)
    print("Days since 01/01/2001:",days)
    print("Day:",Dict_days[DAY])
    Day_Check()

Day_Check()
