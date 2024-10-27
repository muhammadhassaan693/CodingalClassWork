<<<<<<< HEAD
file1 = open("sample2.txt", "r")
file2 = open("sample3.txt", "w")

#reading each line from sample2.txt
for line in file1.readlines():
    if not (line.startswith("good")): #reading all lines that do not begin with the word "good"
        print(line)
        file2.write(line) #writing all lines that do not begin with the word "Good" in to sample3.txt
        
file1.close()
=======
file1 = open("sample2.txt", "r")
file2 = open("sample3.txt", "w")

#reading each line from sample2.txt
for line in file1.readlines():
    if not (line.startswith("good")): #reading all lines that do not begin with the word "good"
        print(line)
        file2.write(line) #writing all lines that do not begin with the word "Good" in to sample3.txt
        
file1.close()
>>>>>>> 62c900b124e1b51f7a08f1cba9b2516d41e0d998
file2.close()