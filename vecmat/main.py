import calc


def main():
    x = calc.vec_gen(3)
    A = calc.matrix_gen(3, 5)
    B = calc.matrix_gen(3, 5)

    print('x=', x)
    print('A=', A)
    print('B=', B)

    a1 = calc.dot_vec_mat(x, A)
    a2 = calc.mult_matrix(A, B)
    a3 = calc.dot_matrix(A, B)

    print('x.A=', a1)
    print('A°B=', a2)
    print('AT.B=', a3)


if __name__ == '__main__':
    main()
