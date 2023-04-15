"""
Name: PATEL DIVYAKUMAR BHARATBHAI
Date: 13/04/2023
Practical: Write a program to create a set of students' enrolment number and sort them and perform addition and deletion operation on it.
"""

setItems = set()

n = int(input("Enter the number of student: "))
for i in range(0, n):
    enroll = int(input(f"Enter the Enroll no. of student-{i+1}: "))
    setItems.add(enroll) # to add item

print(setItems) # without sorted
print() # without sorted
print(set((sorted(setItems)))) # sorted in list form

rem = int(input("Enter the number you want to delete: "))
setItems.discard(rem) # to delete specific item 

print(sorted(setItems))
