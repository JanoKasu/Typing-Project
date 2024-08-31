import os
import LayoutManager
import numpy as np
import json
from matplotlib import pyplot as plt
from GraphVisualization import GraphVisualization

PDFs = os.listdir('./PDFs/')
for file in PDFs:
	if not file.endswith('.pdf'):
		PDFs.remove(file)

##################################################
# Get the data from the PDFs

LayoutManager.get_data(PDFs)

# Get statistics

with open('data.json') as file:
	digrams = json.loads(file.read())['digram']
	keys = list(digrams.keys())
	values = list(digrams.values())

	mean = np.mean(values)
	median = np.median(values)
	standardDeviation = np.std(values)

	print('Mean:\t\t\t', mean)
	print('Median:\t\t\t', median)
	print('Standard deviation:\t', standardDeviation)
	
	fig = plt.figure(figsize = (10, 5))

	# creating the bar plot
	plt.bar(keys, values)
	plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
	plt.show()
	plt.clf()

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
			G.add_edge(start, end[0], end[1])
	
	G.visualize()

##################################################