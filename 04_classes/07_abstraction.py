# abstract methods and classes


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    def stop_engine(self):
        print("Stop Engine")    

class Car(Vehicle):
    def start_engine(self):
        print("Starting the engine")

car = Car()
car.start_engine()
car.stop_engine()
