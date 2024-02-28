# 5.Write a program that opens a file, reads its contents, and writes the contents to a new file. Use a try-except-finally block to ensure
# that the file is closed even if an exception occurs during the file operations.
try:
    with open('qs21.py', 'r') as source_file:
        contents = source_file.read()
    with open('target_file.txt', 'w') as target_file:
        target_file.write(contents)

    print("File contents successfully copied.")

except FileNotFoundError:
    print("Error: Source file not found.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'source_file' in locals():
        source_file.close()
