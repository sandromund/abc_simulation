import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np


def f(x, y):
    return np.sinc((x - 20) / 100 * 3.14) + np.sinc((y - 50) / 100 * 3.14)


def visualize_function(function, n=500):
    x = np.random.rand(n) * 100
    y = np.random.rand(n) * 100
    z = [function(x, y) for _ in range(n)]
    triangulation = tri.Triangulation(x, y)
    data = np.array([x, y, z]),

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.plot_trisurf(triangulation, z, cmap='jet')


# ax.view_init(elev=60, azim=-45)
# ax.scatter(x, y, z, marker='.', s=15, c="black", alpha=0.5)


def update(num):
    line.set_data(data[0:2, :num])
    line.set_3d_properties(data[2, :num])
    return line,


line, = plt.plot(data[0], data[1], data[2], lw=2, c='red')

anim = animation.FuncAnimation(fig, update, frames=100, interval=20, blit=True)

anim.save('plot.gif', writer='imagemagick', fps=30)
