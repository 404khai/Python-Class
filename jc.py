# create a list, add 5 items, print out the last item
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[fruits.__len__() - 1])
print(fruits[-1])
print(type(fruits))

#looping through the list
#for fruit in fruits:
#    print(fruit)

#looping through the list using index
#for i in range(len(fruits)):
#    print(fruits[3])

for fruit in fruits:
    if fruit == "cherry":
        print("Found cherry!")
        

grades = [100, 50, 3, 1213, 65, 89]
grades.sort(reverse=True)
print(grades)

#to make a duplicate copy of a list
myGrades = grades.copy()
myMathGrades = list(grades)

print(myGrades)
print(myMathGrades)

 
# a list is ordered and changeable. Allows duplicate members
# a tuple is ordered and unchangeable. Allows duplicate members
# a set is unordered and unindexed. No duplicate members   
# a dictionary is unordered, changeable and indexed. No duplicate members