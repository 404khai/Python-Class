from Employees import Employee

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def showEmployeeDetails(self):
        super().showEmployeeDetails()
        print(f"Department: {self.department}")

    def calculateBonus(self):
        return self.salary*0.10