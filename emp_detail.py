class employee_details(): 
 
    def __init__(self,name,id): 
        self.name = name 
        self.id = id 
 
    def details(self): 
        company = "spacex" 
        print(f'\nName of employee is "{self.name}" and his id is "{self.id}" 
working in "{company}"') 
 
emp1 = employee_details("James Bond","007") 
emp1.details() 
emp2 = employee_details("John Wick","777") 
emp2.details() 