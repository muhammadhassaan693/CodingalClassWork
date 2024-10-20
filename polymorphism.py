<<<<<<< HEAD
class cat:
    def __init__(self,nm,h):
        self.name = nm
        self.age = h

    def info(self):
        print(f"I am a cat, my name is {self.name} I am {self.age} years old")

    def make_sound(self):
        print("meow")

class dog:
    def __init__(self,nm,h):
        self.name = nm
        self.age = h

    def info(self):
        print(f"I am a dog, my name is {self.name} I am {self.age} years old")

    def make_sound(self):
        print("woof")

#creating object cat and dog
cat1 = cat("snowey", 3)
dog1 = dog("max", 4)

for animal in(cat1,dog1):
    animal.make_sound()
    animal.info()
    print()
=======
class cat:
    def __init__(self,nm,h):
        self.name = nm
        self.age = h

    def info(self):
        print(f"I am a cat, my name is {self.name} I am {self.age} years old")

    def make_sound(self):
        print("meow")

class dog:
    def __init__(self,nm,h):
        self.name = nm
        self.age = h

    def info(self):
        print(f"I am a dog, my name is {self.name} I am {self.age} years old")

    def make_sound(self):
        print("woof")

#creating object cat and dog
cat1 = cat("snowey", 3)
dog1 = dog("max", 4)

for animal in(cat1,dog1):
    animal.make_sound()
    animal.info()
    print()
>>>>>>> 8b0bc7541257b35bde0d0789d3512f52684d99c1
    