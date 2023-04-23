"""
Name: PATEL DIVYAKUMAR BHARATBHAI
Date: 13/04/2023
Practical: Write a program which will allow user to enter 10 numbers and display largest odd and even number from them. Also display the count of odd and even numbers.
"""

import array as ar 

num = ar.array("i", [])
oddCount = 0
evenCount = 0
for i in range(0,10):
    n = int(input(f"Enter {i+1} number: "))
    num.append(n)
    
largestOdd = num[0]
largestEven = num[0]

for i in range(0,10):
    if(num[i] % 2 == 0):
        evenCount = evenCount + 1
        if (num[i] > largestEven):
            largestEven = num[i]
        
    else:
        oddCount = oddCount + 1
        if (num[i] > largestOdd):
            largestOdd = num[i]
            
print("Largest Odd: ", largestOdd)
print("Largest Even: ", largestEven)
print("Odd Count: ", oddCount)    
print("Even Count: ", evenCount)    
