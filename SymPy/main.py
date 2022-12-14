import calc


def main():
    a1 = calc.multi_eqs()
    a2 = calc.limit_calc()
    a3 = calc.diff_calc()
    a4 = calc.antidiff_calc()
    a5 = calc.integral_calc()
    print('a1 =', a1)
    print('a2 =', a2)
    print('a3 =', a3)
    print('a4 =', a4)
    print('a5 =', a5)


if __name__ == '__main__':
    main()
