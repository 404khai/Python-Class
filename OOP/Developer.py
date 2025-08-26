from Employees import Employee

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def showEmployeeDetails(self):
        super().showEmployeeDetails()
        print(f"Language: {self.language}")
