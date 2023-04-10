'''
Name: PATEL DIVYAKUMAR BHARATBHAI
Date: /04/2023
lab: 1
practical 1.2: Write a program in python to implement menu driven simple calculator.
'''

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponential\n6. Exit")
i = True
while (i == True):
    
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter your choice: "))

    match c:
        case 1:
            print(a + b)
        case 2:
            print(a - b)
        case 3:
            print(a * b)
        case 4:
            print(a / b)
        case 5:
            print(a ** b)
        case 6:
            print("Bye...")
            break
        case _:
            print("Enter valid number!!!")

    d = int(input("Do you want to continue?(yes: 1 || no: 0) "))
    if(d == 0):
        print("Bye...")
        break

"""
#
# We can solve it using if elif also.
#
    if c == 1:
        print(a+b)
    elif c == 2:
        print(a - b)
    elif c == 3:
        print(a * b)
    elif c == 4:
        print(a / b)
    elif c == 5:
        print(a ** b)
    elif c == 6:
        print("Bye...")
        i = False
    else:
        print("Enter valid number")

"""