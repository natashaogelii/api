class Vehicle():
    def start_engine(self):
        res = "engine started"
        return res


    def stop_engine(self):
        pass



class Car(Vehicle):
    pass


car = Car()
print(car.start_engine())