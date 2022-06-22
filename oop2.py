class Teacher:
    def __init__(self,name,salary,deseg):
        self.name=name
        self.salary=salary
        self.deseg=deseg
    @classmethod
    def from_str(cls,stri):
        # name,salary,deseg=stri.split(",")    line --1 
        # return cls(name,salary,deseg)       line  ---2
        return cls(*stri.split("-"))          #line --3 ... line 1 ,line 2=line3
t1=Teacher.from_str('waqar-29999-teacher')
print(t1.name)
print(t1.salary)
