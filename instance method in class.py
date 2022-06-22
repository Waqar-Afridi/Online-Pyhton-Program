class person:
    def __init__(self,Fname,Lname,age):
        self.Fname=Fname
        self.Lname=Lname
        self.age=age
    def full_name(self):
        return f" First_name is {self.Fname}  last_name is {self.Lname} "
        # print( f" First_name is {self.Fname}  last_name is {self.Lname} ") ...> dono ka kam hai print and return
    def is_above_18(self):
        return self.age>18





p1=person('waqar','ahmad',24)
p2=person("amin",'ullah',17)
print(p1.full_name())
print(person.is_above_18(p2))  # p1 . full_name and
                               # person.is_above_18(p2) are same working