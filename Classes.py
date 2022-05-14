import datetime
class Employee:
    # Class variables - it can be anything:
    num_of_emp = 0
    raise_amt = 1.04

    # initionalization (construct) of the class, contains instance variables:
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.' + last + '@company.com'
        self.pay = pay

    # special methods:
    def __repr__(self):
        return "Employee ('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    # Regular method - must have self argument:
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # Class methods - the first argument is the class:
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static method - accepts any argument we want to, don't access instance or class variables:
    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True

# a creation of a child class:
class Developer(Employee):
    # polymorfism - change a value of an object from the parent class:
    raise_amt = 1.10
    # initialization of the child class:
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # it is the same as Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

# another child class:
class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # add employee to the employees list:
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    # remove employee from the employees list:
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # print the employee list:
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())




emp_1 = Employee('Cory', 'Scafer', 5000)
emp_2 = Employee('Test', 'User', 6000)

#print using the method - the brackets (partnthesis) are empty:
print(emp_1.fullname())
#print from the class itself:
print(Employee.fullname(emp_1))
#another way:
print(emp_1.fullname)

# print class variable:
print(Employee.raise_amt)

# change class method:
Employee.set_raise_amt(1.05)
# NOT to do but it's possible: change class method from the instance:
emp_1.set_raise_amt(1.05)

# create a new employee:
emp_str_3 = 'Joe-Doe-90000'
first, last, pay = emp_str_3.split('-')
# create emp_3:
new_emp_3 = Employee(first, last, pay)
print(new_emp_3.email)
print(new_emp_3.pay)

# a creation of a new employee from the class method!:
new_emp_3 = Employee.from_str(emp_str_3)

# using static method:
my_date = datetime.date(2017, 7, 10)
print(Employee.is_workday(my_date))

# presentation of emp_1 due to __repr__ method:
print(emp_1)

# 2 ways to call special functions:
# through the instance:
print(repr(emp_2))
print(str(emp_2))
# or directly:
print(new_emp_3.__repr__())
print(new_emp_3.__str__())

# aritmetic special functions:
#for int:
print(int.__add__(1,2))
# for str:
print(str.__add__('a', 'b'))

# sum of 2 employees payments due to __add__ special function:
print(emp_1+ emp_2)

# print(len(test)) is equal to print('test'.__len__())
print(len(emp_1))

dev_1 = Developer('Cory', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.email)
print(dev_1.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)

# print the list of employees of manager 1:
mgr_1.print_emps()

# add another employee to manager 1:
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

# remove an employee from manager 1:
mgr_1.remove_emp(dev_2)

print(isinstance(mgr_1, Employee))
print(issubclass(Manager, Developer))