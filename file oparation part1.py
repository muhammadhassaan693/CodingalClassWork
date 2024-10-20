file = open("sample2.txt","r")

print("raeding all of the content in the file")
print(file.read())
file.close()

print()

file = open("sample2.txt","r")
print("reading the first eight character")
print(file.read(8))

file.close()