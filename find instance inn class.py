class Laptop:
    count_instance=0
    def __init__(self,Brand_name, Model_name,price):
        Laptop.count_instance+=1
        self.Brand_name=Brand_name
        self.Model_name=Model_name
        self.price=price


l1=Laptop('haeir' ,'m3', 30000)
l2=Laptop('hp', 'axu34', 370000)
l3=Laptop('apple', 'mac', 300000)

print(Laptop.count_instance)



# def method3(name='khan',*var):
#     print("this is method 3")
#     print("your name is :",name)
#     for x in var:
#        print("value of ",x)
#     else:
#        print("waqar")
# method3('ahmad',2)
