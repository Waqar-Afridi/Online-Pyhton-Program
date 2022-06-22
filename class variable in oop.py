class Laptop:
    per_num=10  # class varible
    def __init__(self,Brand_name, Model_name,price):

        self.Brand_name=Brand_name
        self.Model_name=Model_name
        self.price=price
    def apply_discount(self):
        perr_num= (Laptop.per_num/100)*self.price # in this statement we use class varible
        return self.price-perr_num

l1=Laptop("heair",'M3',65000)
l2=Laptop("Hp",'5th',45000)
print(l1.apply_discount())