class phone:  # Base class or parent class
    def __init__(self,Brand_name,Model_name,price):
        self.Brand_name=Brand_name
        self.Model_name=Model_name
        self.price=price
    def make_a_call(self,phone_number):
        return f'calling {phone_number}....'

    def full_name(self):
        return  f" Brand Name is  :{self.Brand_name}: and Model name :{self.Model_name}:"

class smartphone(phone): #drived class or child class

    def __init__(self,Brand_name,Model_name,price,ram,rear_camera):
        phone.__init__(self, Brand_name, Model_name, price) # ye zyda use nahi hoti
        super().__init__(Brand_name,Model_name,price)
        self.ram=ram
        self.rear_camera=rear_camera

class flagshipphone(smartphone):  # multi level inheritance
    def __init__(self, Brand_name, Model_name, price, ram, rear_camera,fornt_camera):
        super().__init__(Brand_name, Model_name, price, ram, rear_camera)
        self.fornt_camera=fornt_camera


        #making object and calling function
phone1=phone('nokia' , '3310',134568)
smartphone1=smartphone('apple','12promix',200000,'8GB','20mp')
print(phone1.full_name()+ f" price is {phone1.price}")
print(smartphone1.full_name()+f'price is {smartphone1.price } and ram is{smartphone1.ram} and camera is {smartphone1.rear_camera}')
oneplus=flagshipphone('samsung','a71',200000,'8GB','20mp','50mp')
print(oneplus.full_name())

