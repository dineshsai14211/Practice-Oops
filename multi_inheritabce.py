class Bike:

    def __init__(self,cc,color,brand):
        self.cc=cc
        self.color=color
        self.brand=brand
class Bike1:

    def __init__(self,name):
        self.name=name
    
class Bike2(Bike,Bike1):

    def __init__(self,name,cc,color,brand,length):
        self.length=length
        Bike.__init__(self,cc,color,brand)  
        Bike1.__init__(self,name)
        
print("*******Bike class Attribute values***********")
B=Bike("160","Red","yamaha")
print(f'CC = {B.cc} \ncolor = {B.color} \nBrand = {B.brand}')
print("*******Bike1 class Attribute values********")
B1=Bike1("Hunter350")
print(f'Name = {B1.name}')
print("*******Bike2 class Attribute values***************")
B2=Bike2("pulsar","250","black","Bajaj","350m")
print(f'Name = {B2.name} \nCC = {B2.cc} \ncolor = {B2.color} \nBrand = {B2.brand} \nLength = {B2.length}')

