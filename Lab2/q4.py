# question 4: You are developing a simple employee management system. The base class Employee has a method work(). Derived classes like Manager, Developer, and Designer override
# work() with tasks specific to their role. Students should create objects of each employee type and call work() to 
# show how polymorphism allows the same method name to perform different actions.

class Employee:
    def work(self):
        print("Base Class: Employee.")

class Manager(Employee):
    def work(self):
        print("Child Class: Manager.")

class Developer(Employee):
    def work(self):
        print("Child Class: Developer.")

class Designer(Employee):
    def work(self):
        print("Child Class: Designer.")

e = Employee()
e.work()

e = Manager()
e.work()

e = Developer()
e.work()

e = Designer()
e.work()
