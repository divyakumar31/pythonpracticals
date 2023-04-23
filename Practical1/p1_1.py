"""
Name: PATEL DIVYAKUMAR BHARATBHAI
Date: 13/04/2023
Practical: Write a program to Convert Celsius to Fahrenheit and vice –a-versa based on the choice of user.
"""

print("1. Celsius to Fahrenhiet \n2. Fahrenhiet to Celsius")
ch = int(input("Enter your choice: "))

if (ch == 1):
    celsius = int(input("Enter the value in Celsius: "))
    fahrenhiet = ((celsius * 9)/5) + 32
    print("Fahrenhiet: ", fahrenhiet)

else:
    fahrenhiet = int(input("Enter the value in Fahrenhiet: "))    
    celsius = ((fahrenhiet - 32) * 5)/9 
    print("Celsius: ", celsius)

