import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np


def visualize_function(n=500):
    x = np.random.rand(n) * 100
    y = np.random.rand(n) * 100
    z = np.sinc((x - 20) / 100 * 3.14) + np.sinc((y - 50) / 100 * 3.14)
    triangulation = tri.Triangulation(x, y)
    data = np.array([x, y, z]),
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.plot_trisurf(triangulation, z, cmap='jet')
    return fig


if __name__ == '__main__':
    fig = visualize_function()
    plt.show()
