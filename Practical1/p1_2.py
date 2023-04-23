"""
Name: PATEL DIVYAKUMAR BHARATBHAI
Date: 13/04/2023
Practical: Write a program in python to implement menu driven simple calculator.
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("1. addition\n2. subtraction\n3. Multiplication\n4. Division\n5. Exponential")
c = int(input("Enter your choice: "))

if (c == 1):
    print(a+b)
elif (c == 2):
    print(a-b)
elif (c == 3):
    print(a*b)
elif (c == 4):
    print(a/b)
elif (c == 5):
    print(a**b)
else:
    print("Enter valid choice")