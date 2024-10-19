file = open("sample1.txt", "w") #open the file in write mode

#rewriting the file 
file.write("file in the write mode")
file.write("\n hello nice to meet you ")

#closing the file
file.close()

#open the file in append mode
f = open("sample1.txt", "a")

#adding the new content in the file
f.write("\n \n this is new content and we combined it with the privious content")

f.close()