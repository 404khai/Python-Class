from Manager import Manager
from Developer import Developer
from rest import Calculator
from bank import BankAccount

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


#Polymorphism
employees = [
    Manager("Mario", 4500, "HR"),
    Developer("Daniel", 7000, "Python")
]

for employee in employees:
    print(f"{employee.name}'s Bonus: {employee.calculateBonus()}")


acc = BankAccount("Prince", 45000)
acc.deposit(45000)
print(acc.getBalance())