file_read = open("Codingal.txt", "r")
print("File in read mode.. ")
print(file_read.read())
file_read.close()

file_write = open("Codingal.txt", "w")
file_write.write("File in write mode..")
file_write.write("Hi i am Bharath.")
file_write.close()

file_append = open("Codingal.txt", "a")
file_append.write("\n File in append mode..")
file_append.write("Hello I am Bharth.")
file_append.close()