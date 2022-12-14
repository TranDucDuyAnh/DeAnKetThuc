import numpy as np
import matplotlib.pyplot as plt


def get_list_value():
    x = np.linspace(start=-10, stop=10, num=1000)
    y0 = x**4 - 2*x**2 - 3
    y1 = 4*x**3 - 4*x
    y2 = 12*x**2 - 4
    y3 = 24*x
    return x, y0, y1, y2, y3


def draw_plot(x, y0, y1, y2, y3):
    fig, ax = plt.subplots()

    ax.plot(x, y0, label=r'$y = x^{4} - 2x^{2} - 3$')
    ax.plot(x, y1, label=r'$y = 4x^{3} - 4x$')
    ax.plot(x, y2, label=r'$y = 12^{2} - 4$')
    ax.plot(x, y3, label=r'$y = 24x$')

    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")

    ax.set_title("Đồ thị $y = x^{4} - 2x^{2} - 3$")

    ax.legend()
    plt.show()