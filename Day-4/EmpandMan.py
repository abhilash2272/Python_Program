class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def display(self):
        print(f"Salary of {self.name} is {self.sal}")
class Manager(Employee):
    def __init__(self,name,sal,dept):
        super().__init__(name,sal)
        self.dept=dept
    def display(self):
        print(f"Salary of {self.name} is {self.sal} of department {self.dept}")
e=Employee("abhi",9999)
print("Employee details")
e.display()
m=Manager("shiva",99999,"Medical-coding")
print("Manager details")
m.display()
