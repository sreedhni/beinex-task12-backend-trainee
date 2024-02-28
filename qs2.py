# 2.Create a program that opens a file and reads its contents. Use a try-except block to handle the FileNotFoundError exception and 
# display a custom error message if the file does not exist

try:
    file_name = input("Enter the file name: ")
    with open(file_name, "r") as file:  
        contents = file.read()
        if contents:
            print("Contents of the file:")
            print(contents)
        else:
            print("This is an empty file.")
except FileNotFoundError:
    print("Error: The specified file does not exist.")

