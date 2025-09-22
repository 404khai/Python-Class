# a = 36
# print(a)

# print(2==2)
# print('mike'=='Mike')
#print(2!=1)

# def add(a,b):
#     return a + b
# print(add(2, 3))

# sum = add(45, 458)
# print(f'sum' = sum)

# def userAge(age):
#     if age < 18:
#         return 'You are not eligible'
#     return 'Congratulations'

# print(userAge(90))

# def studentScore(score):
#     grade = " "
#     if score >= 70 and score <=100:
#         grade = "A"
#     elif score <= 60:
#         grade = "B"
#     elif score <= 50:
#         grade = "C"
#     else:
#         grade = "F"
#     return grade

# stdGrade = studentScore(100)

# prefix = ""
# if stdGrade == "A":
#     prefix = "an"

# print("You scored" + " " + prefix + " " + stdGrade)


# Question: A town has a unique traffic rule based on your speed and weather. It is your birthday the fine varies
# def speedProgram(speed, isBirthday):
#     if speed <= 60:
#         print("No fine")
#     elif isBirthday == False and (speed > 60 or speed <= 80):
#         print("Small fine") 
#     elif isBirthday == True and (speed > 60 or speed <= 80):
#         print("No fine") 
#     elif isBirthday == False and (speed > 80):
#         print("Big fine")
#     elif isBirthday == True and (speed > 80):
#         print("Small fine")

    
# print(speedProgram(71, True))

# def determine_fine(speed: int, is_birthday: bool) -> str:
#     if speed <= 60:
#         return "No fine"
#     elif 61 <= speed <= 80:
#         return "No fine" if is_birthday else "Small fine"
#     else:  # speed > 80
#         return "Small fine" if is_birthday else "Big fine"

# print(determine_fine(55, False))  
# print(determine_fine(75, True))   
# print(determine_fine(75, False))  
# print(determine_fine(85, True))   
# print(determine_fine(85, False))  

# x = 12

# c = complex(x)
# print(c)

a = "Danielle"
print(a.lower()) 

intro = "Hello, my name is {} and I am {} years old."
print(intro.format('John', 15))
intro2 = "Hello my name is"
name = 'john'
age = 15

print(intro2+" " + name + " " + "and I am" + " " + str(age) + " " + "years old.")