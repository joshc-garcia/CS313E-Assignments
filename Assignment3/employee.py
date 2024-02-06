"""
File: employee.py
Description: Program that represents various employees that a company may have. 
Student Name: Joshua Garcia
Student UT EID: jcg4725
Partner Name:
Partner UT EID:
Course Name: CS 313E
Unique Number: 50775
Date Created: 02/05/2024
Date Last Modified: 02/05/2024
"""
#################################################################################################

class Employee:
    """Class that represents an employee."""
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.identifier = kwargs.get('identifier')
        self.salary = kwargs.get('salary')

    def __str__(self):
        return f'{self.__class__.__name__}\n{self.name} {self.identifier} {self.salary}'

#################################################################################################

class PermanentEmployee(Employee):
    """Class that inherits employee attributes, as well as includes benefits."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs.get('benefits')

    def cal_salary(self):
        """Calculates salary based on benefit package."""
        if self.benefits == ['health_insurance']:
            salary = 0.9 * self.salary
        elif self.benefits == ['retirement']:
            salary = 0.8 * self.salary
        elif self.benefits == ['retirement', 'health_insurance']:
            salary = 0.7 * self.salary
        return salary

    def __str__(self):
        return f'{Employee.__str__(self)} {self.benefits}'

#################################################################################################

class TemporaryEmployee(Employee):
    """Class that inherits employee attributes, but salary is based on worked hours."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs.get('hours')

    def cal_salary(self):
        """Calculates salary based on hours worked and hourly pay."""
        salary = self.salary * self.hours
        return salary

    def __str__(self):
        return f'{Employee.__str__(self)} {self.hours}'

#################################################################################################

class Consultant(TemporaryEmployee):
    """Class that inherits temp employee attributes. Salary includes travel bonus."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs.get('travel')

    def cal_salary(self):
        """Calculates salary based on Temp salary, as well as travel bonus."""
        salary = TemporaryEmployee.cal_salary(self) + (self.travel * 1000)
        return salary

    def __str__(self):
        return f'{Employee.__str__(self)} {self.hours} {self.travel}'

#################################################################################################

class Manager(Employee):
    """Class that inherits employee attributes. Salary includes bonus."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs.get('bonus')

    def cal_salary(self):
        """Calculates salary based on total salary and bonus."""
        salary = self.salary + self.bonus
        return salary

    def __str__(self):
        return f'{Employee.__str__(self)} {self.bonus}'

#################################################################################################

class ConsultantManager(Consultant, Manager):
    """Class that inherits from the consultant and manager classes. Salary is based on
    bonus, hours worked, and travel."""
    def cal_salary(self):
        salary = (self.salary * self.hours) + (self.bonus) + (self.travel * 1000)
        return salary

    def __str__(self):
        return f'{Employee.__str__(self)} {self.hours} {self.travel}'

#################################################################################################

def main():
    """
    A Main function to create some example objects of our classes.
    """
    chris = Employee(name="Chris", identifier="UT1")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", identifier="UT2",
                            salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = TemporaryEmployee(name="Sam", identifier="UT3", salary=100, hours=40)
    print(sam, "\n")

    john = Consultant(name="John", identifier="UT4", salary=100, hours=40,
                        travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", identifier="UT5",
                        salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = ConsultantManager(name="Matt", identifier="UT6",
                            salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    print("Check Salaries")
    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:", matt.cal_salary(), "\n")

if __name__ == "__main__":
    main()
