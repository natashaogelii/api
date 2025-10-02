
class Car():
    def start(self):
        print("Starting the engine")

class EvCar():
    def start(self):
        print("Strating the EV")


def start_engine(car_type):
    car_type.start()

new_car = Car()
start_engine(new_car)

new_evcar = EvCar()
start_engine(new_evcar)