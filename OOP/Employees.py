class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def showEmployeeDetails(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")