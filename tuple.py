mytuple=(7, "pizza", 17, 4.9, "soda")
print(mytuple)

#accessing tuple elemeant using index
print(mytuple[1])

print()

#nested taple
ntuple=("watermelon", 63, ("fanta", "pepsi", 5.3))
print(ntuple)
print(ntuple[1])
print(ntuple[2])

car = ("Opel", "Corsa", 2015, "1.3cc")
timetable = [
    ("Maths", "English", "Social"),
    ("English", "Sports", "Computer")
]
print(f"Timetable for 2nd day {timetable[1]}") #Show me the classes on the 2nd day

classTimeTable = {
    "Mon": ("Maths", "English", "Social"),
    "Tue": ("English", "Sports", "Computer")
}
print(f"Timetable for Tuesday {classTimeTable["Tue"]}") #Show me the classes on Tuesday