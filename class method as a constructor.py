class person:
    def __init__(self,fname ,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
    @classmethod  # class method as constructor and its syntax
    def from_str(cls,strrng):
        fname,lname,age=strrng.split(",")
        return cls(fname,lname,age)
p1=person.from_str("waqar,ahmad,24")
# print(person.from_str("waqar,akhn,23"))