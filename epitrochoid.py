import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the constants
R = 3
r = 1
d = 1 / 2

# Create the figure and the axes
fig, ax = plt.subplots()

# Define the graph limits
ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))

# Define the functions for the x and y coordinates
def x(t):
    return (R + r) * np.cos(t) - d np.cos((R + r) / r * t)

def y(t):
    return (R + r) * np.sin(t) - d np.sin((R + r) / r * t)

# Define the animation update function
def update(num):
    # Delete the previous points
    ax.clear()

    # Create a series of values for t
    t = np.linspace(0, num / 10, num)

    # Obtain the corresponding values of x and y
    xs = x(t)
    ys = y(t)

    # Draw the Epitrochoid curve
    ax.plot(xs, ys)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, repeat=False)

# Show the animation
plt.show()
