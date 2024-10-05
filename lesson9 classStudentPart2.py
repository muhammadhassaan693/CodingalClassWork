class student:
    grade=7
    name="Muhammad hassaan"

    #creating a method
    def introduction(self):
        print("hi I am a student")

    def detail(self):
        print(f"my name is {self.name}")
        print(f"I study in grade {self.grade}")

#creating class object
obj=student()
obj.introduction()
obj.detail()
