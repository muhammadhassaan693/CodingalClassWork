#parent class
class person(object):
    def __init__(self, nm, idn):
        self.name=nm
        self.idnumber=idn
    
    def display(self):
        print(f"name = {self.name}")
        print(f"id number = {self.idnumber}")

#child class
class employee(person):
    def __init__(self, nm, idn, pay, post):
        self.salary = pay
        self.post=post

        person.__init__(self, nm, idn)

#create object
h=employee("ali", 716, 2500, "full time employee")
h.display()
    