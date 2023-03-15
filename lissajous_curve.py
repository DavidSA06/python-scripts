import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the constants
A = 1
B = 1.5
a = 2
b = 3

# Create the figure and the axes
fig, ax = plt.subplots()

# Define the graph limits
ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))

# Define the functions for the x and y coordinates
def x(t):
    return A * np.sin(a * t)

def y(t):
    return B * np.sin(b * t)

# Define the animation update function
def update(num):
    # Borramos los puntos anteriores
    ax.clear()

    # Creamos una serie de valores para t
    t = np.linspace(0, num / 10, num)

    # Obtenemos los valores de x e y correspondientes
    xs = x(t)
    ys = y(t)

    # Draw the Lissajous curve
    ax.plot(xs, ys)

# Creamos la animación
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, repeat=False)

