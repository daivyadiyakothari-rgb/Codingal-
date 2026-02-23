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