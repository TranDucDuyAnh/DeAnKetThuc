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


def main():
    x = vec_gen(3)
    A = matrix_gen(3, 5)
    B = matrix_gen(3, 5)

    print('x=', x)
    print('A=', A)
    print('B=', B)

    a1 = dot_vec_mat(x, A)
    a2 = mult_matrix(A, B)
    a3 = dot_matrix(A, B)

    print('x.A=', a1)
    print('A°B=', a2)
    print('AT.B=', a3)


if __name__ == '__main__':
    main()
