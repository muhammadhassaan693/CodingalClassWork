#reading the first line of the file
file = open("sample2.txt", "r")
print("reading the first line")
print(file.readline())
file.close()

print()

#reading the first two lines of the file
file = open("sample2.txt", "r")
print("reading multiple lines")
print(file.readline())
print(file.readline())
file.close()