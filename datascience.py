import numpy as np

np.random.seed(0) # seed for reproucability

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr2 = np.random.randint(2, 10, size=(2,3))
print(arr2)

# indexing some element
a1 = arr1[0]
a2 = arr2[0][1]
print("arr[0] should print 1. Check: " + str(a1))

# indexing some element from end of array
b1 = arr1[-2]
b2 = arr2[-2][-3]
b3 = arr2[0][0]

print("arr[-2] should print 9. Check: " + str(b1))

if b2 == b3:
    print("arr2[-2][-3] and arr2[0][0] are accessing the same element of arr2 ")
else:
    print("Something went wrong")

subarr2_a = arr2[:, :2]
subarr2_b = arr2[:, :-1]
# print(subarr2_a)
# print(subarr2_b)

# using NumPy arrays in boolean context: for == use the following:
if subarr2_a.all() == subarr2_b.all():
    print("arr2[:,:2] and arr2[:,-1:] are accessing the same element of arr2 ")
else:
    print("Something went wrong")
