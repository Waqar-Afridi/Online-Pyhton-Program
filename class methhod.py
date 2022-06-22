class person:
    count_instance=0
    def __init__(self,fname,lname,age):
        person.count_instance+=1
        self.fname=fname
        self.lname=lname
        self.age=age
    @classmethod   # creating of class method syntax
    def count_instances(cls): # here argument will be is a class name
        return f" your have created {cls.count_instance}  instances of person class"

p1=person('waqar','ahmaad',24)
p2=person('waqar','ahmaad',24)
p3=person('waqar','ahmaad',24)
print(person.count_instances())
print(p1.fname)







# aziz assigment

# def method1(id,name):
#     print("hi  is method1",id ,name)
#     print("your id is : ",id)
#     print("your name is :",name)
# method1(22,'khan')