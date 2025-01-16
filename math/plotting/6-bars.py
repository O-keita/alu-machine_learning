#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

people = ['Farrah', 'Fred', 'Felicia']
fruit_labels = ['apples', 'bananas', 'oranges', 'peaches']
fruit_colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

x = np.arange(len(people))
bar_width = 0.5

bottom = np.zeros(len(people))
for i in range(len(fruit)):
    plt.bar(x, fruit[i], width=bar_width, label=fruit_labels[i], color=fruit_colors[i], bottom=bottom)
    bottom += fruit[i]

plt.xlabel("Person", fontsize='small')
plt.ylabel("Quantity of Fruit", fontsize='small')
plt.title("Number of Fruit per Person", fontsize='small')
plt.xticks(x, people, fontsize='small')
plt.yticks(np.arange(0, 81, 10), fontsize='small')
plt.ylim(0, 80)
plt.legend(loc="upper right", fontsize='small')

plt.tight_layout()
plt.show()
