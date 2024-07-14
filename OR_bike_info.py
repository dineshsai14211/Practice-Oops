class Bike():
    def __init__(self, name):
        self.name = name

    def bike_name(self):
        return f'Name of bike is= {self.name}'


class Bike1(Bike):
    def bike_name(self):
        return f'Name of bike is "{self.name}" it is a 2024 model'


person = Bike1("Triumph")
print("Override method returns is= ",person.bike_name())  # the method name (bike_name) is overrided in child class then the method in parent class
