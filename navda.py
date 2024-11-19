# def drdo(n):
#     k=''
#     for i in str(n):
#         k+=str(int(i)**2)
#     return int(k)
# n=int(input())
# print(drdo(n))



# def srt(s):
#     j=''
#     a=sorted(s,key=len)
#     for h in a:
#         k=str(h)+' '
#         j+=k
#     return j
# l=input('enter a list of student names')
# s=l.split()
# print(srt(s))
n=int(input())
d={}
for i in range(n):
    s=input()
    l=s.split()
    a=l[0]
    b=int(l[1])
    k={a:b}
    d.update(k)
print(d)


#oops
# class Student:
#     "documentation string"

# print(Student.__doc__)
# help(Student)

# #def __init__(self,name,rollno,marks):
#     self.name=name
#     self.rollno=rollno
#     self.marks=marks

# class test:
#     def __init__(self):
#         print("Construction execution")
#     def m1(self):
#         print("Method execution...")0
# t1=Test()
# t2=Test()
# t3=Test()
# t1.m1()

# class Car:
#     def __setenginemodel__(self,engine):
#         print(engine)
#     def __getenginemodel__(self,engine):
#         print(engine)
# class 
#     def __setcarmodel__(self,model):
#         print(model)
#     def __getcarmodel__(self,model):
#         print(model)
# mycar=Honda()
# mycar.setenginemodel('EK-1')
# mycar.setenginemodel('v6')
# print('Car det')

# class person:
#     def setname(self, name):
#         self.name = name
        
#     def getname(self):
#         print(self.name)
        
# class student(person):
#     def setage(self, age):
#         self.age=age
        
#     def getage(self):
#         print(self.age)
        
# class address(student):
#     def setaddress(self, address):
#         self.address=address
#     def getaddress(self):
#         print(self.address)

# s1 = address()
# name = input()
# age = int(input())
# place = input()

# s1.setname(name)
# s1.setage(age)
# s1.setaddress(place)

# s1.getname()
# s1.getage()
# s1.getaddress()

# class Test:
#     def __init__(self):
#         self.__x=10
#     def __m1(self):
#         print("pvt m1 method")
#     def m2(self):
#         print(self.__x)
#         self.__m1()
# t= Test()
# t.m2()
# print(t.__x)
# t.__m1()

# class student:
#     def _init_(self, name, roll_no):
#         self.__name=name
#         self.__roll_no=roll_no
#     def m1(self):
#         print(self.__name)
#         print(self.__roll_no)

# s = student("Arya",19)
# s.m1()
# s.__name

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__group = "ECE" 
        self.__report = "fail"  

    def set_details(self, group, report):
        self.__group = group
        self.__report = report

    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Group: {self.__group}")
        print(f"Report: {self.__report}")
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
group = input("Enter student's group: ")
report = input("Enter student's report (pass/fail): ")
student = Student(name, age)
student.set_details(group, report)
student.get_details()
