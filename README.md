# Networks Visualization

## Vertices

### 1. ```class```

```python
class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

### 2. Tuples

```python
vertex = (x, y)
```

## Edges

Add an edge between ```vertices[i] and vertices[j]```

```python
plt.plot([vertices[i].x, vertices[j].x], [vertices[i].y, vertices[j].y], 'b')  # the 'b' parameter displays a blue edge
```
