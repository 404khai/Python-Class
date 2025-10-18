# create a list, add 5 items, print out the last item
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[fruits.__len__() - 1])
print(fruits[-1])
print(type(fruits))

for fruit in fruits:
    print(fruit)
# a list is ordered and changeable. Allows duplicate members
# a tuple is ordered and unchangeable. Allows duplicate members
# a set is unordered and unindexed. No duplicate members   
# a dictionary is unordered, changeable and indexed. No duplicate members