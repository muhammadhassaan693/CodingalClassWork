#dictionary with intiger keys
mydictionary={1:"apple",
            2:"PINEAPPLE",
            3:"grapes"}

print(mydictionary)

#accessing the data using the key
print(mydictionary[2])
print(mydictionary.get(2))

#dictionary with mixed keys
people={"name":"muhammad",
        "age":26,
        3:"antalya"}

print()
print(people)

print()

#adding new item
people["country"]="turkey"
print(people)