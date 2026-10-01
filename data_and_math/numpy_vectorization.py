import numpy as np
# Scalar arithmatic
array = np.array([1, 2, 3, 4])
# Some basic operations we can perform;
print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)
# Vectorized math functions
array1 = np.array([47, 56, 29, 83])
# Some basic math functions are;
print(np.sqrt(array1))
print(np.round(array1))
print(np.floor(array1))
print(np.ceil(array1))

# A small project with radi function
# take radi(i)(us) as user input

radii = np.fromstring(input("Enter radii separated by spaces: "), sep=" ")

if radii.size == 0: #Just to be sure it's not empty
    print("Please enter at least one radius.")
    exit()

# Perform calculation for Area of Cirlce which is pi*radi**2 ( for each )
areas = np.pi * (radii ** 2)
print("Calculated Areas:", areas)  # Finally Print the areas
