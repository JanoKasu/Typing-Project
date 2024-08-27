import os
import LayoutManager
from GraphVisualization import GraphVisualization
import json

PDFs = os.listdir('./PDFs/')
for file in PDFs:
	if not file.endswith('.pdf'):
		PDFs.remove(file)

##################################################
# Get the data from the PDFs

LayoutManager.getGraph(PDFs)

##################################################
# Visualize Graph

with open("graph.json") as f:
	G = GraphVisualization()
	data = json.load(f)
	# start is the element in the dictionary that points to a list of other elements
	for start in data:
		# end is the list of elements that start points to
		for end in data.get(start):
			# end[0] is  the letter, end[1] is the weight
			G.addEdge(start, end[0], end[1])
	
	G.visualize()
# Alg.minimize()