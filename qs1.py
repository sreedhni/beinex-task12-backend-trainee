# Write a Python program that prompts the user to enter an integer and handles the ValueError exception if the user enters a non-integer value.


while True: #The while loop is used in this program to repeatedly prompt the user to enter an integer value until a valid input is provided.
    try:
        integer_value = int(input("Enter an integer value: "))
        print("This is the user entered integer value:", integer_value)
        break  # Break out of the loop if a valid integer is entered
    except ValueError:
        print("Please enter a valid integer value.")
