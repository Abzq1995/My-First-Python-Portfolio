"""num1 and num2 are variables , however they are strings so will not work as integers. so strings will need to be
converted in to integers"""
'''However a more quicker way would be to enter this code below. Depending if you want integer you enter int first or 
if you want a decimal , you type float first.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
result = num1 + num2'''

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2

'''The conversion can be done by adjusting the result section like this result = int(num1) + int(num2).
Result however will not calculate decimals so , if calculating decimals input code as 
result = float(num1) + float(num2) '''

print(result)
