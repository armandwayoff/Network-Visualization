import matplotlib.pyplot as plt
import random

vertices = []

# create 10 vertices
for _ in range(10):
    new_vertex = (random.uniform(0, 1), random.uniform(0, 1))
    vertices.append(new_vertex)

for vertex in vertices:
    plt.plot(vertex[0], vertex[1], 'ro')
plt.show()
