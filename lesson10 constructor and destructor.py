<<<<<<< HEAD
class employee:
    #initializing constructor
    def __init__(self):
        print("employee created")

    #deleting the object (destructor)
    def __del__(self):
        print("destructor is called and employee is deleted")

obj=employee()
=======
class employee:
    #initializing constructor
    def __init__(self):
        print("employee created")

    #deleting the object (destructor)
    def __del__(self):
        print("destructor is called and employee is deleted")

obj=employee()
>>>>>>> 8b0bc7541257b35bde0d0789d3512f52684d99c1
del obj