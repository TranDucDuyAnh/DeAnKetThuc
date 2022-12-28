from sympy import *


# Viết hàm giải hệ phương trình
def multi_eqs():
    # Define Variables
    x, y, z = symbols('x y z')
    # Define Equations
    eq1 = Eq(2*x - 5*y + z, -5)
    eq2 = Eq(4*x + 2*y - 2*z, 2)
    eq3 = Eq(x + y - z, 0)
    # Solve the Equations
    ans = solve((eq1, eq2, eq3), (x, y, z))
    return ans


# Viết hàm tính giới hạn
def limit_calc():
    # Define Variables
    x = symbols('x')
    # Build Equations
    f = cbrt(x**3 - 3*x**2) + sqrt(x**2 - 2*x)
    # Solve the Problem
    ans = limit(f, x, +oo)
    return ans


# Viết hàm tính đạo hàm
def diff_calc():
    x = symbols('x')
    f = (2*x-1)/(x+2)
    ans = diff(f, x)
    return ans


# Viết hàm tính nguyên hàm
def antidiff_calc():
    x = symbols('x')
    f = x/(x**2+1)
    ans = integrate(f, x)
    return ans


# Viết hàm tính tích phân
def integral_calc():
    x = symbols('x')
    f = (1 - x*tan(x))/(x*x*cos(x) + x)
    ans = integrate(f, (x, 2*pi/3, pi))
    return ans
