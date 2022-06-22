class phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def make_a_call(self,phone_number):
        return f'we calling to {phone_number}.....'

    def full_name(self):
        return f'{self.brand} {self.model}'

phone1=phone("realme",'m5',2500)
print(phone1.make_a_call(89008909877))
print(phone1.full_name())