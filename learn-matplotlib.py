# Matplotlib is a library that helps to generate plots, histograms, bar charts etc

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
# returns an array of equal distance items.
# first argument represents starts point
# second argument represents the end point
# third argument represents the number of items to be generated
y = x ** 2

print(x)
print(y)

# There are 2 ways of plotting:
# 1. Functional programming
plt.plot(x, y)
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Gold prices')
# plt.show()
plt.subplot(1, 2, 1)  # arguments: 1 - number of rows | 2. number of columns | 3. the index number of subplot
plt.subplot(1, 2, 2)  # the last argument here, gets the number 2 to fill in the missing area in the canvas
# plt.plot(x, y, 'red')
# plt.show()

# 2. Object Oriented programming
fig = plt.figure(figsize=(8, 2))  # figsize sets the dimensions of the figure
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# first 2 arguments (0.1,0.1) represent he starting point of the drawing.
# the second 2 arguments (0.8, 0.8) represnt the relative sizing from the canvas (80%)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')
plt.plot(x,y,'g')
plt.show()

fig2 = plt.figure()
axes1 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])
axes1.set_xlabel('X Label')
axes1.set_ylabel('Y Label')
axes2 = fig2.add_axes([0.1, 0.1, 0.5, 0.5])
axes2.set_xlabel('X Label')
axes2.set_ylabel('Y Label')
plt.plot(x, y, 'g', label='X squared')  # label here defines what will be displayed in the legend
axes2.legend(loc=(0.1, 0.1)) # generated a legend at (0.1, 0,1)
plt.show()

# for in depth info about plot styling, see part three of matplotlib
axes1.set_xlim([0, 1]) # crops between given values (0,0 to 1,2)
axes1.set_ylim([0, 2])

print(type(axes))
print(type(fig))

# subplots
fig, axes = plt.subplots(nrows=1, ncols=2)  # this method accept fig (the empty figure)
# and the Axes as values and generates a subplot with 1 row and 2 columns
axes[0].plot(x, y, color='g')  # plots the values of x vs. y in the first subplot
axes[1].plot(y, x, 'b')
plt.tight_layout()  # handles overlapping subplots by spreading them
plt.show()  # prints the subplots

fig.savefig('myfig.png', dpi=300)  # saves a figure (dpi (dots per inch)
