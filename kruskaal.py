class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = []
	
	def add_edge(self, u, v, w):
		self.graph.append([u, v, w])
		
	def find(self, parent, x):
		if parent[x] != x:
			parent[x] = self.find(parent, parent[x])
		return parent[x]

	def union(self, parent, x, y):
		xset = self.find(parent, x)
		yset = self.find(parent, y)
		
		parent[yset] = xset
	
	def kruskal(self):
		result = []

		i = 0
		e = 0
		
		self.graph = sorted(self.graph, key=lambda item: item[2])

		parent = []
		for node in range(self.V):
			parent.append(node)

		while e < self.V - 1:
			u, v, w = self.graph[i]
			i += 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			if x != y:
				e += 1
				result.append([u, v, w])
				self.union(parent, x, y)
		
		for x in result:
			print(f"{x[0]+1} - {x[1]+1}: {x[2]}")

g = Graph(7)
# Create the 
g. add_edge(4, 6, 12)
g. add_edge(3, 4, 11)
g. add_edge(1, 4, 10)
g. add_edge(0, 1, 9)
g. add_edge(1, 3, 8)
g. add_edge(3, 6, 7)
g. add_edge(5, 6, 6)
g. add_edge(3, 5, 5)
g. add_edge(2, 5, 4)
g. add_edge(2, 3, 3)
g. add_edge(0, 3, 2)
g. add_edge(0, 2, 1)

g.kruskal()