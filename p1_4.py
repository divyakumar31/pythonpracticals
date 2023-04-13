"""
Name: PATEL DIVYAKUMAR BHARATBHAI
Date: 13/04/2023
Practical: Write a Python program to check if the number provided by the user is a Prime number. Perform it with and without user defined function.
"""

# Without Function
num = int(input("Enter the number: "))
flag = True

for i in range(2, num):
    if (num % i == 0):
        print(f"{num} is not a Prime number.")
        flag = False
        break

if(flag):
    print(f"{num} is Prime Number.")


# With Function
def PrimeNumber(num):
    flag = True

    for i in range(2, num):
        if (num % i == 0):
            print(f"{num} is not a Prime number.")
            flag = False
            break

    if(flag):
        print(f"{num} is Prime Number.")


number = int(input("Enter the number: "))        
PrimeNumber(number)
