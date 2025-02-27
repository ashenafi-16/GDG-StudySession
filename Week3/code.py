class Vehicle:
    def __init__(self, make, model):
        self._make = make
        self._model = model

    def describe(self):
        return f"a vehicle - Make: {self._make}, Model: {self._model}"

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def set_make(self, make):
        self._make = make

    def set_model(self, model):
        self._model = model

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)  
        self._num_doors = num_doors  

    def describe(self):
        return f"This is a Car - Make: {self.get_make()}, Model: {self.get_model()}, Doors: {self._num_doors}"

    def get_num_doors(self):
        return self._num_doors

    def set_num_doors(self, num_doors):
        self._num_doors = num_doors

class Bike(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)  

    def describe(self):
        return f"This is a Bike - Make: {self.get_make()}, Model: {self.get_model()}"

def vehicle_description(vehicle):
    print(vehicle.describe())

car = Car("Toyota", "Camry", 4)
bike = Bike("Yamaha", "YZF-R1")

vehicle_description(car)  
vehicle_description(bike)  
