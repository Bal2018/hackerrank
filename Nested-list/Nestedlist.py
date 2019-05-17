# hackerrank - Used Python 3 
#!/bin/python3
 
def is_leap(year):              #function to check if year is a LEAP year
leap = False
    if (year%4==0):             #check if year is divisable by 4
        leap=True
        if (year%100==0):       #check if year is divisable by 100
            leap=False
            if (year%400==0):   #check if year is divisable by 400
                leap=True
return leap

year = int(input())
print(is_leap(year))