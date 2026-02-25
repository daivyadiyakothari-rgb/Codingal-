# Activty 1
file_read = open('Codingal.txt')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# Activity 2
file_write = open('Codingal.txt', 'w')
file_write.write("File in write mode....")
file_write.write("Hi! I am Penguin. I am 1 year old")
file_write.colse()

# Activity 3
file_line = open('Codingal.txt','r')
print("File in Read Mode -")
print(file_line.readlines())
file_line.close()

# Activity 4
file_append = open('Codingal.txt', 'a')
file_append.write("\nFile in append mode....")
file_append.write("Hi! I am Penguin. I am 3 year old")
file_append.close()

# After Class Project
names = ["Diya", "Daivya", "Divolka", "Diva"]

# Write mode
with open("students.txt", "w") as file:
    file.write("Student Introduction List\n")
    file.write("-------------------------\n")

# Append mode
with open("students.txt", "a") as file:
    for i in range(len(names)):
        file.write(str(i + 1) + ". My name is " + names[i] + "\n")

# Read mode
with open("students.txt", "r") as file:
    print(file.read())

# Read and Write mode
with open("students.txt", "r+") as file:
    old_content = file.read()
    file.seek(0)
    file.write("Class Monitor: Arnav\n\n" + old_content)