class Car:

    #initialize
    def __init__(self, brand, color):
        self.car_brand = brand
        self.car_color = color  #what about self.color

#You can get input as well
brand = input("Car Brand")
color = input("Car Color")

c = Car("VW", "Black")
print(c.car_brand)
print(c.car_color)