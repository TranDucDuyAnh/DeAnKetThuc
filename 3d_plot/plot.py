import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


# Viết hàm vẽ đồ thị mặt yên ngựa
def saddle():
    x = np.linspace(start=-3, stop=3, num=500)
    y = np.linspace(start=-3, stop=3, num=500)

    x, y = np.meshgrid(x, y)
    z = (x/3)**2 - (y/2)**2

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    saddle_surf = ax.plot_surface(x, y, z, cmap=cm.copper, linewidth=0)

    ax.set_zlim(-4, 4)
    fig.colorbar(saddle_surf, shrink=0.5, aspect=5)
    ax.set_title("Yên ngựa")

    plt.show()


# Viết hàm vẽ đồ thị mặt hyperbolic 1 tầng
def hyperboloid():
    x = np.linspace(start=-10, stop=10, num=500)
    y = np.linspace(start=-10, stop=10, num=500)

    x, y = np.meshgrid(x, y)
    z = np.sqrt(((x/3)**2 + (y/5)**2 + 1)*4)

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    saddle_surf = ax.plot_surface(x, y, z, cmap=cm.winter, linewidth=0)

    ax.set_zlim(1, 6)
    fig.colorbar(saddle_surf, shrink=0.5, aspect=5)
    ax.set_title("Hyperbolic 1 lớp")

    plt.show()


# Viết hàm vẽ đồ thị mặt cầu:
def sphere(a: int, b: int, c: int, radius: int):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = (np.outer(np.cos(u), np.sin(v)) * radius) + a
    y = (np.outer(np.sin(u), np.sin(v)) * radius) + b
    z = (np.outer(np.ones(np.size(u)), np.cos(v)) * radius) + c

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    sph = ax.plot_surface(x, y, z, cmap=cm.jet, linewidth=0)
    fig.colorbar(sph, shrink=0.5, aspect=5)
    ax.set_title("Hình cầu")

    plt.show()
