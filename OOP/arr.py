import numpy as np

#arr = np.array([1,2,3,4,5])

#arr = np.array((45)) #0 dimensional array
#print(type (arr))

#arr = np.array(([1,2,4], [5,6,7]))

#print(arr)

#arr = np.array((([1,2,3], [4,5,6], [7,8,9])))
#print(arr.ndim)

# arr = np.array([1,2,3,4], ndmin=6)
# print(arr)
# print(arr.ndim)

#list = [10,20,30,40,50]
#print(lst)

# arr = np.array([10,20,30])
# print(arr[1])

#arr = np.array([[1,2,3], [4,5,6], [30,40,50]])
#print(arr[2,0])   #arrays are numbered in the order 0,1,2. picked by index array 0, index 2 is 3

#print(arr.dtype)

#fruits = np.array(["mango","apple","banana","orange"])
#prin9t(fruits.dtype)

#arr = np.array([1,2,3,4,5])
#newArr = arr.astype('i')
# print(arr)
# print(newArr.dtype)

#arr = np.array([[1,2,3], [4,5,6], [30,40,50]])
# print(arr.shape)
# print(arr.size)

# print(arr[0,0]) #row 0, column 0

# print(np.random.rand(10,10))

sales = np.array([
    [30, 50, 70], #day 1
    [10, 20, 30],
    [60, 50, 10],
])

#print("Sales Data: ", sales)
#print("Total per product: ", sales.sum(axis=0))

print("Average eggs sold: ", sales[::,2].mean())