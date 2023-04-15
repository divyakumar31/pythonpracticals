"""
Name: PATEL DIVYAKUMAR BHARATBHAI
Date: 13/04/2023
Practical: Write a program to create a dictionary of student details- EnrollmentNo, Name, Branch and perform addition and deletion of entry of key-value pair form it.
"""

def insertItem():
    roll = int(input("Enter roll no: "))
    name = input("Enter the your name: ")
    branch = input("Enter the branch: ")
    student[roll] = [name, branch]


def deleteItem():
    de = int(input("Enter enroll number: "))
    student.pop(de)


def displayItem():
    di = int(input("Enter enroll no to display details: "))
    print("Name: ", student[di][0])
    print("Branch: ", student[di][1])



student = {115 : ["Dev", "CE"], 123 : ["Jabar", "ME"], 129 : ["Divy", "BE"]}

# to insert item
print("1. Insert \n2. Delete \n3. Display \nOtherwise exit")
while(True):
    ch = int(input("Enter your choice: "))
    if (ch == 1):
        insertItem()
    elif (ch == 2):
        deleteItem()
    elif (ch == 3):
        displayItem()
    else:
        exit()

