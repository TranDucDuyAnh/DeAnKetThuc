import numpy as np


def vec_gen(n):
    x = np.random.randint(low=1, high=10, size=n)
    return x


def matrix_gen(m, n):
    A = np.random.randint(low=1, high=10, size=m*n).reshape((m, n))
    return A


# Cho x ∈ Rn và A ∈ Rm×n, hãy viết hàm tính tích x.A
def dot_vec_mat(x, A):
    ans = np.dot(x, A)
    return ans


# Cho A, B ∈ Rm×n, hãy viết hàm tính A°B và AT.B
def mult_matrix(A, B):
    ans = np.multiply(A, B)
    return ans


def dot_matrix(A, B):
    A_chvi = A.T
    ans = np.dot(A_chvi, B)
    return ans
