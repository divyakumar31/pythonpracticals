"""
Name: PATEL DIVYAKUMAR BHARATBHAI
Date: 13/04/2023
Practical: Write a program to create a tuple to students CPI and display it.
"""

listItem = []
n = int(input("Enter the number of student: "))
for i in range(0, n):
    cpi = int(input(f"Enter the CPI of student-{i+1}: "))
    listItem.append(cpi)
    
tupleItem = tuple(listItem)

while (True):
    ch = int(input("Enter the enroll no of student you want to see CPI: "))
    if (ch > (n+1) or ch < 1):
        print("Student not found.")
    else:
        print(tupleItem[ch-1])

    run = input("Do you want to continue?(Y/N) ")
    if ( not (run == 'Y' or run == 'y')):
        break

