mylist=[7,9,"apple",3.5,"pineapple", False] #list with multipul data types

print(mylist)
print("first element of my list= ",mylist[0])
print("second element of my list= ",mylist[1])
print("last element of my list= ",mylist[4])
print("last element of my list= ",mylist[-1])

print("lenght of the list=",len(mylist)) #counting how many data in the list

#adding new element 
mylist.append(15)
print("updated list=",mylist)

#removing the element
mylist.remove(9)
print("updated list after removing the deta=",mylist)

#removing the first element using the index
mylist.pop(0)
print("updated list after removing the data based on the index=",mylist)
print()

#list with the same data type
furitlist=["watermelon","orange","grape"]
print(furitlist)

#sorting the list using
furitlist.sort()
print("sorted list= ",furitlist)

#reverse the list
furitlist.reverse()
print("reverse list= ",furitlist)