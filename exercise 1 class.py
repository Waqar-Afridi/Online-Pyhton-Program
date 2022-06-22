class Laptop:
    def __init__(self,Brand_name, Model_name,price):
        print("this is constructer ....")
        print()
        self.Brand_name=Brand_name
        self.Model_name=Model_name
        self.price=price

l1=Laptop("heair",'M3',30000)
l2=Laptop("Hp",'5th',45000)
print(f"The Brand_Name is {l1.Brand_name}\n And The Model_Name is {l1.Model_name}\n And The Price is {l1.price}")
print(" ")
print(l2.Brand_name)
print(l2.Model_name)
print(l2.price)