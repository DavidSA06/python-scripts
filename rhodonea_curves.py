import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the constants
A = 1
B = 1
n = 2
d = 3

# Create the figure and the axes
fig, ax = plt.subplots()

# Define the graph limits
ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))

# Define the functions for the x and y coordinates
def x(t):
    return A * np.cos(n / d * t)* np.cos(t)

def y(t):
    return B * np.cos(n / d * t)* np.sin(t)

# Define the animation update function
def update(num):
    # Delete the previous points
    ax.clear()

    # Create a series of values for t
    t = np.linspace(0, num / 10, num)

    # Obtain the corresponding values of x and y
    xs = x(t)
    ys = y(t)

    # Draw the Rhodonea curve
    ax.plot(xs, ys)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, repeat=False)

# Show the animation
plt.show()
