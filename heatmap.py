import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100)#genrates a matrix of equispaced elements from 0 to 100 
y = np.arange(100)


#meshgrid returns the multi dimensional array from two or more component dimension  
# You need to capture the TWO arrays meshgrid returns
X, Y = np.meshgrid(x, y) #meshgrid breaks into columns(Y) and rows(X) 
print(X)
print()
print("................................")
print()
print(Y)

#refrence point 
cx, cy = 50, 50

print()
print("................................")

#manhatana formula 
# Use the 2D grids (X and Y) for the calculation
distance_matrix = np.abs(X - cx) + np.abs(Y - cy)
print(distance_matrix)

# Now distance_matrix.shape is (100, 100), which imshow expects
plt.imshow(distance_matrix, cmap='magma')
plt.colorbar(label='Manhattan Distance')
plt.show()
