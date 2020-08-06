import matplotlib.pyplot as plt
import random

vertices = []

# create 10 vertices
for _ in range(10):
    new_vertex = (random.uniform(0, 1), random.uniform(0, 1))
    vertices.append(new_vertex)

for i in range(len(vertices) - 1):
    plt.plot([vertices[i][0], vertices[i + 1][0]], [vertices[i][1], vertices[i + 1][1]], 'b')

for vertex in vertices:
    plt.plot(vertex[0], vertex[1], 'ro')
plt.show()
