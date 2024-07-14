class Bikes(): 
    name1 = "pulsar n160" 
    Cc1 = 160 
    name2= "triumph 400" 
    Cc2 = 400 
 
    def bike1(self): 
        print(f'Name of bike is "{self.name1}" and it has "{self.Cc1}" Cc') 
 
    def bike2(self): 
        print(f'Name of bike is "{self.name2}" and it has "{self.Cc2}" CC') 
 
obj = Bikes() 
print("Accessing the bike1 method") 
obj.bike1() 
print("\nAccessing the bike2 method") 
obj.bike2()