# i am implementing eigen decomposition and svd in this file 
import numpy as np
import scipy.linalg

C = np.array([[-3, 5, -5], [-7, 9, -5], [-7, 7, -3]])
evals, evecs = scipy.linalg.eig(C)

# evals is a 1D array of eigenvalues, evecs is the matrix P of eigenvectors
D = np.diag(evals.real) # Create the diagonal matrix D from eigenvalues
P = evecs
print("Eigenvalues (D):", D.diagonal())
# Reconstruct the original matrix
Pinv = scipy.linalg.inv(P) # Calculate the inverse of P
A_reconstructed = P @ D @ Pinv
# Check with np.allclose(A_reconstructed, C)
