#writing mode
file = open("sample2.txt", "w")
file.write("Hello, this is the first line in the file.\n")
file.write("File handling in Python is easy to learn.\n")
file.close() 
print("Data written successfully.\n")

#reading mode
file = open("sample2.txt", "r")
print("Reading file contents:")
content = file.read()
print(content)
file.close() 

#append mode
file = open("sample2.txt", "a")
file.write("This line is added using append mode.\n")
file.close()
print("\nData appended successfully.\n")

# Read the file again to see updated content
file = open("sample2.txt", "r")
print("Updated file contents:")
print(file.read())
file.close()
