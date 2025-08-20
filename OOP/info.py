#class info():
#    greet = "How are you doing"

#print(info)
#info1 = info()

#print(info1.greet)

class Person():
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def __str__(self):
        return f"Fullname: {self.firstName} {self.lastName}"
    
    def user_details(self):
        return f"Name: {self.firstName} {self.lastName}" 
    
p1 = Person("Daniels", "Fega")
p2 = Person("Sam", "Wilson")
#p1.lastName = "Prince"
#print(p1)
print(p1.user_details())