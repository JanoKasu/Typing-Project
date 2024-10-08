import networkx as nx 
import matplotlib.pyplot as plt 

class GraphVisualization: 

	def __init__(self): 
		# visual is a list which stores all the set of edges that constitutes a graph 
		self.visual = [] 
		
	# addEdge function inputs the vertices of an edge and appends it to the visual list 
	def add_edge(self, a, b, w): 
		self.visual.append([a, b, w])
		
	# In visualize function G is an object of class Graph given by networkx G.add_edges_from(visual) creates a graph with a given list 
	# nx.draw_networkx(G) - plots the graph 
	# plt.show() - displays the graph 
	def visualize(self):
		G = nx.Graph()
		G.add_weighted_edges_from(self.visual)
		pos = nx.spring_layout(G, seed=7)

		# Draw the nodes
		nx.draw_networkx_nodes(G, pos, node_size=250)

		# Draw the edges
		nx.draw_networkx_edges(G, pos, width=1)

		# Draw the labels
		# node labels
		nx.draw_networkx_labels(G, pos, font_size=6, font_family="sans-serif")

		# edge weight labels
		"""
		edge_labels = nx.get_edge_attributes(G, "weight")
		colors = []
		for key in edge_labels:
			colors.append(edge_labels[key])
		nx.draw_networkx_edge_labels(G, pos, edge_labels)
 		"""
		
		# Show
		ax = plt.gca()
		ax.margins(0.08)
		plt.axis("off")
		plt.tight_layout()
		plt.savefig('./images/SpringGraph.png')
		plt.show()
