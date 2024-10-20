<<<<<<< HEAD
class computer:
    def __init__(self):
        self.__maximum_price=900 #making the variable private

    def sell(self):
        print(f"maximum price is {self.__maximum_price}")

    def set_maxmum_price(self,price):
        self.__maximum_price= price

#creating object
c=computer()
c.sell()

#trying to chance the maximum price
c.__maximum_price=1000
=======
class computer:
    def __init__(self):
        self.__maximum_price=900 #making the variable private

    def sell(self):
        print(f"maximum price is {self.__maximum_price}")

    def set_maxmum_price(self,price):
        self.__maximum_price= price

#creating object
c=computer()
c.sell()

#trying to chance the maximum price
c.__maximum_price=1000
>>>>>>> 8b0bc7541257b35bde0d0789d3512f52684d99c1
c.sell 