class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def raisee(self):
        print(f"Employee name: {self.name}")
        print(f"Salary: {self.salary}")
emp_name = input("Enter the employee's name: ")
emp_1 = Employee(emp_name, 25000)