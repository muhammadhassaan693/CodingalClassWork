#displaying stars in inrows and colum
#by using nested loops
x=int(input("enter the number of rows= "))

for i in range(0,x): #outer loops for displaying rouus
    for j in range(0,i+1): #iner loops for displaying colums
        print("*",end=" ")
    
    print("\n")
