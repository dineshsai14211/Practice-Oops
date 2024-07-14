class Bike:

    def __init__(self,cc,color,brand):
        self.cc=cc
        self.color=color
        self.brand=brand

    def detail(self):
        return f'"{self.name}",it has "{self.cc}" cc comes with color "{self.color}" of "{self.brand}" brand '
class Bike1(Bike):

    def __init__(self,name,cc,color,brand):
        self.name=name
        super().__init__(cc,color,brand)
    
class Bike2(Bike1):

    def __init__(self,name,cc,color,brand,length):
        self.length=length
        super().__init__(name,cc,color,brand)

bike=Bike2("Scrambler 400","400","Red and Black","Triumph","150cm")
bike1=Bike2("Pulsar 200","200","Gradiate Black","Bajaj","175m")
print("Accessing 'detail' method through object,where Bike2 class acquired property from Bike1 it acquired from Bike class which has method 'detail'")
print("Specifications of Bike:-\n",bike.detail())
print("**********************************************")
print("Specifications of Bike:-\n",bike1.detail())