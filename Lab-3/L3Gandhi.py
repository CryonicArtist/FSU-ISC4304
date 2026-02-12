import matplotlib.pyplot as plt
import numpy as np

# Data generation
n_samples = 50000
x = np.random.normal(10, 5, n_samples)
y = np.random.gamma(1.4, 20, n_samples)

# Added a grid
fig = plt.figure(figsize=(10, 10))
grid = plt.GridSpec(4, 4, hspace=0.3, wspace=0.3)

# Main graph
ax_main = fig.add_subplot(grid[1:4, 0:3])
ax_main.hist2d(x, y, bins=100, range=[[-50, 50], [0, 75]], cmap='viridis', density=True)

# AI Prompt used for x/y concentration graphs: "I made a density graph of random x,y values as shown in the code attached. 
# Generate marginal histograms for x and y seperatly. Make sure they are lined up with the main density graph as shown in the screenshot"

# X axis concentration graph
ax_x_dist = fig.add_subplot(grid[0, 0:3], sharex=ax_main)
ax_x_dist.hist(x, bins=100, range=(-50, 50), color='teal', density=True)

# Y axis concentration graph
ax_y_dist = fig.add_subplot(grid[1:4, 3], sharey=ax_main)
ax_y_dist.hist(y, bins=100, range=(0, 75), orientation='horizontal', color='teal', density=True)



plt.show()