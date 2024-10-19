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
print(f"area = {rect.area()}")