# 3.Write a program that calculates the division of two numbers entered by the user. Use a try-except block to handle the ZeroDivisionError 
# exception and display an appropriate error message if the user tries to divide by zero.

while True:
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        break  
    except ValueError:
        print("Error: Please enter valid numerical values.")

try:
    division_answer = number1 / number2
    print(f"{number1} / {number2} = {division_answer}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.zero division error")
