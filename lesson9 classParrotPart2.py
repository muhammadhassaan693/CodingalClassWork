class parrot:
    species="bird" #this is class atbriute
    
    #instance method
    def __init__(self,nm,h):
        self.name=nm
        self.age=h

    def sing(self,song):
        return f"{self.name} sings a {song} song"

#creating the object
blue=parrot("Blue",3)

#access class atribute
print(f"Blue is a {blue.species}")
print(f"{blue.name} is {blue.age} years old")

#calling the method
print(blue.sing("happy"))