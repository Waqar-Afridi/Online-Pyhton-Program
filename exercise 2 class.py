class Laptop:
    def __init__(self,Brand_name, Model_name,price):

        self.Brand_name=Brand_name
        self.Model_name=Model_name
        self.price=price
    def apply_discount(self,per_num):
        perr_num= (per_num/100)*self.price
        return self.price-perr_num

l1=Laptop("heair",'M3',65000)
l2=Laptop("Hp",'5th',45000)
print(l2.apply_discount(10))