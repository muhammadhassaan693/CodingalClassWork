<<<<<<< HEAD
#parent class
class person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname

    def print_name(self):
        print(f"fullname = {self.firstname} {self.lastname}")

class student(person):
    def __init__(self, fn, ln, year):
        super().__init__(fn, ln)
        self.graduation_year=year

#creating the object
x = student("muhammad", "hassan", 2025)
x.print_name()
=======
#parent class
class person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname

    def print_name(self):
        print(f"fullname = {self.firstname} {self.lastname}")

class student(person):
    def __init__(self, fn, ln, year):
        super().__init__(fn, ln)
        self.graduation_year=year

#creating the object
x = student("muhammad", "hassan", 2025)
x.print_name()
>>>>>>> 8b0bc7541257b35bde0d0789d3512f52684d99c1
print(f"graduation year = {x.graduation_year}")