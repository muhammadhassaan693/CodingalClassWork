class employee:
    #initializing constructor
    def __init__(self):
        print("employee created")

    #deleting the object (destructor)
    def __del__(self):
        print("destructor is called and employee is deleted")

obj=employee()
del obj