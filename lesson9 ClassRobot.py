class robot:
    origin="pakistan"
    name="class bot 2.0"

    #creating a method
    def introduction(self):
        print("hi I am a robot")

    def detail(self):
        print(f"my name is {self.name}")
        print(f"my origin is {self.origin}")

#creating class object
obj=robot()
obj.introduction()
obj.detail()