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

    ax.plot(x, y0, label=r'$y = x^{4} - 2x^{2} - 3$', marker=".")
    ax.plot(x, y1, label=r'$y = 4x^{3} - 4x$', marker="^")
    ax.plot(x, y2, label=r'$y = 12x^{2} - 4$', marker="x")
    ax.plot(x, y3, label=r'$y = 24x$', marker="D")

    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")

    ax.set_title("Đồ thị $y = x^{4} - 2x^{2} - 3$")

    ax.legend()
    plt.show()


def main():
    x, y0, y1, y2, y3 = get_list_value()
    draw_plot(x, y0, y1, y2, y3)


if __name__ == '__main__':
    main()
