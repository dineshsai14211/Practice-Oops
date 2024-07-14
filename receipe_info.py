import re
class biriyani():

    def __init__(self,Meat,Rice,water=None,spices=None):
        self.Meat=Meat
        self.Rice=Rice
        self.water=water
        self.spices=spices
        pattern=r"\d+"
        res=re.match(pattern,self.Rice)
        res=res.group()
        if int(res)==1:
            #for 1kgs of rice require 1ltr water
            self.water="1ltr"
        else:
            self.water="2ltr"
       
    def ingredients(self):
        print(f'Required ingredients for making biriyani is \nMeat = {self.Meat},\nRice = {self.Rice},\nwater = {self.water},\nspices = {self.spices}')

print("------Person requiremnts-------")
meat=int(input("Enter which meat is require \n1)Chicken \n2)Mutton = "))
rice = int(input("Enter how much amount rice is required in kgs \n1) 1kgs \n2) 2kgs = "))
spices = input("Spices are Required or Not Required = ")
meat_list=["Chicken","Mutton"]
meat_cond=True
while True:
    while meat_cond!=False:
        if meat==1:
            meat=meat_list[0]
            meat_cond=False
            break
        elif meat==2:
            meat=meat_list[1]
            meat_cond=False
            break
        meat=int(input("You've Choosen wrong option,Choose 1)Chicken 2)Mutton = "))
    if rice==1:
        rice="1kgs"
        break
    elif rice==2:
        rice="2kgs"
        break
    rice=int(input("You've Choosen Wrong Option ,Choose 1)1kgs 2)2kgs = "))

person1=biriyani(meat,rice,spices=spices)
print("**************************************************")
person1.ingredients()
print("**************************************************")

