def checkAge (age):
    if age < 18:
        return "Unqualified"
    else:
        return "Congrats"

print(checkAge(10))
print(checkAge(20))