class Teacher:
    def __init__(self,name,salary,deseg):
        self.name=name
        self.salary=salary
        self.deseg=deseg
    def Teacher_details(self):
        return f" Teacher name is {self.name} . salary is {self.salary} and designation is {self.deseg}"

t1=Teacher('ali',23000,'teacher')
print(t1.Teacher_details())

# print(t1.name)