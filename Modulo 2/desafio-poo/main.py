from abc import ABC, abstractmethod

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Employee(ABC): #A class that has a metaclass derived from ABCMeta cannot be instantiated
    @abstractmethod 
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    def get_hours(self):
        return 8

class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__department = Department('managers', 1) #protected attribute

    def calc_bonus(self):
        return self.salary * 0.15

    def get_department(self):
        return self.__department.name #return department's name

    def set_department(self, department):
        self.__department.name = department #change department's name

class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__department = Department('sellers', 2)
        self.__sales = 0 #not to touch it from outside the class, private attribute

    def get_department(self):
        return self.__department.name #return department's name

    def set_department(self, department):
        self.__department.name = department #change department's name

    def get_sales(self):
        return self.__sales

    def put_sales(self, sales):
        self.__sales += sales #add values to attribute

    def calc_bonus(self):
        return self.__sales * 0.15