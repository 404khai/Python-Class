from Manager import Manager
from Developer import Developer
from rest import Calculator

# empl = Manager("Nathan", 5000, "IT")
# emp2 = Developer("Prince", 2300, "Java")

# empl.showEmployeeDetails()
# print()
# print("**__________****__________****___________**")
# print()
# emp2.showEmployeeDetails()



# calc = Calculator()
# print(calc.add(2, 8))
# print(calc.add(1, 3))
# print(calc.add(9, 5, 6))

employees = [
    Manager("Mario", 4500, "HR"),
    Developer("Daniel", 7000, "Python")
]

for employee in employees:
    print(f"{employee.name}'s Bonus: {employee.calculateBonus()}")


