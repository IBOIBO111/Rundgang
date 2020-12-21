import numpy as np
import scipy as sp

A = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

Diagon = np.diagonal(A)
U = np.triu(A,k=1)
L = np.tril(A,k=-1)

t1 = np.subtract(A,U)
D = np.subtract(t1,L)

M = np.subtract(A,U)
N = -U
#A = M - N
#M = (D + L) and N = -U
Pinv = sp.linalg.inv(M)
x_k_1 = np.dot(Pinv,np.dot(N,x_k)) + np.dot(Pinv,b)


print(U)
print(L)
print(D)
input("das wars!")