"""
Name: PATEL DIVYAKUMAR BHARATBHAI
Date: 13/04/2023
Practical: Write a program to create a list of ten numbers entered by user and find smallest and largest number from the list and display it.
"""

listItem = []

for i in range(0,10):
    n = int(input(f"Enter list item-{i+1}: "))
    listItem.append(n)


print(listItem)
listItem.sort()
print("Smallest number from list: ", listItem[0])
print("Largest number from list: ", listItem[9])
