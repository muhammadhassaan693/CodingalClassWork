<<<<<<< HEAD
class parrot:
    species="bird" #this is class atbriute
    
    #instance method
    def __init__(self,nm,h):
        self.name=nm
        self.age=h

#creating the object
blue=parrot("Blue",3)

#access class atribute
print(f"Blue is a {blue.species}")
=======
class parrot:
    species="bird" #this is class atbriute
    
    #instance method
    def __init__(self,nm,h):
        self.name=nm
        self.age=h

#creating the object
blue=parrot("Blue",3)

#access class atribute
print(f"Blue is a {blue.species}")
>>>>>>> 8b0bc7541257b35bde0d0789d3512f52684d99c1
print(f"{blue.name} is {blue.age} years old")