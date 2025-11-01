class Basic:
    degree="B.tech" #This class object variable
    def __init__(self,name,age):
        self.student_name=name
        self.student_age=age
    def display(self,branch):
        self.student_name="karan"  #updating variable
        print(f"This is {self.student_name} , my age is {self.student_age} and my degree is {self.degree} ")#Basic.degrre it is also possible
        return branch

student1=Basic("Jessie",22)
#student1.student_naame="Jessie"->It is okay but not efficient 
print(student1.student_name)
print(student1.display("cse"))