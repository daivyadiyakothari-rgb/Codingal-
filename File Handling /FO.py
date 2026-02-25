# Activity 1
file = open("Codingal.txt", "r")
print(file.read())
file.close()

# Activity 2
file_read = open('Codingal.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file = open('Codingal.txt', 'a')
file_write = ("File in write mode")
file_write.write("hi! I am a penguin and I am 1 year old")
file.close()

file_append = open('Codingal.txt', 'a')
file_append.write("File in append mode")
file_append.write("I am a penguin and I am 1 year old")
file_append.close()

# Activity 3
file1 = open('Codingal.txt', 'r')
file2 = open('CodingalUpdated.txt', 'w')
for line in file1.readlines():
    if not (line.startswith('Coding')):
        print(line)
        file2.write(line)
file2.close()
file1.close()

# Activity 4
fn = open('Codingal.txt', 'r')
fn1 = open('CodingalUpdated.txt', 'w')
cont = fn.readlines()
type(cont)
for i in range (1, len(cont), 2):
    if(i % 2 !=0):
        fn1.write(cont[i])
    else:
        pass
fn1.close()
fn1 = open('CodingalUpdated.txt', 'r')
cont1 = fn1.read()
print(cont1) 

fn.close()
fn1.close()