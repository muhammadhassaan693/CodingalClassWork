<<<<<<< HEAD
#parent class
class shape:
    def __init__(self, w, l, n):
        self.width = w
        self.name = n
        self.length = l

    def printDetail(self):
        print(f"shape = {self.name}")
        print(f"width = {self.width}")
        print(f"length = {self.length}")

#child class
class rectangle(shape):
    def __init__(self, wi, le):
        shape_name = "rectangle"
        super().__init__(wi, le, shape_name)

    def area(self):
        return self.width * self.length

#creating object
x = 5
y = 2
rect = rectangle(x, y)
rect.printDetail()
=======
#parent class
class shape:
    def __init__(self, w, l, n):
        self.width = w
        self.name = n
        self.length = l

    def printDetail(self):
        print(f"shape = {self.name}")
        print(f"width = {self.width}")
        print(f"length = {self.length}")

#child class
class rectangle(shape):
    def __init__(self, wi, le):
        shape_name = "rectangle"
        super().__init__(wi, le, shape_name)

    def area(self):
        return self.width * self.length

#creating object
x = 5
y = 2
rect = rectangle(x, y)
rect.printDetail()
>>>>>>> 02f91c365eeab9cb87ad1fa9bed3b63f8a07bd30
print(f"area = {rect.area()}")