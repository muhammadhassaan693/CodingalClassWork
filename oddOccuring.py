def oneOddOccuring(array1):
    result = 0

    for element in array1 :
        result = result ^ element

    return result

myList = []
listSize = int(input("Enter the array / list size = "))

while listSize:
    number = int(input("Enter the number for your array element = "))
    myList.append(number)
    listSize = listSize - 1

print(f"my list is {myList}")

print()

OddOccuring_number = oneOddOccuring(myList)
print(f"odd occuring number is {OddOccuring_number}")