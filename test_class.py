#EXAMPLE_1------>
class Person:
    count = 0 
    #init--> تابع شروع هست به اصطلااح self--> همیشه باید باشه
    def __init__(self, name, age):
        #self--> اشاره میکنه به همون متغیر
        self.name = name
        self.age = age
        Person.count += 1
    def get_name(self):
        print(f"name is {self.name}: ")
    def get_age(self):
        print(f"age is {self.age}: ")
    def get_info(self):
        print(f"name is {self.name} and age is {self.age}.")
    def get_birthday(self):
        self.age =+ 1
        print(f"happy birthday {self.name}")
    def return_count(self):
        return(Person.count)

#instances نمونه ها: 
jadi = Person("jadi", 40)
jadi.get_name()
jadi.get_info()
jadi.get_birthday()
jadi.get_age()
print(f"at the moment i have {jadi.return_count()}")

maryam = Person("maryam", 20)
maryam.get_name()
maryam.get_info()
maryam.get_birthday()
maryam.get_age()


#EXAMPLE_2------->

class Computer:
    count = 0
    def __init__(self, ram, hard, cpu):
        Computer.count += 1
        self.ram = ram
        self.hard = hard
        self.cpu = cpu

    def value(self):
        return self.ram+self.hard+self.cpu
    def __del__(self):
        Computer.count -= 1 
        
    
class Laptop(Computer):
    def value(self):
        return self.ram+self.hard+self.cpu+self.size

pc1 = Computer(12, 2, 4)
print(pc1.value())
del pc1

laptop1 = Laptop(16, 2, 4) 
print (laptop1.value())       






