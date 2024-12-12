#encapsulation
'''class Student:
    id=int(input('enter the ID:'))
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name:,{self.name}\nage=,{self.age}")
a=input('enter=')
s=Student(a)
s.display()
print(s.id)'''
#2
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
name=input('enter the name=')
salary=int(input('enter the salary='))
emp=Employee(name,salary)
print('name:',emp.name)
print('salary:',emp.salary)
