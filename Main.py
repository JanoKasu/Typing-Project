import os
import LayoutManager
import json
from matplotlib import pyplot as plt
from GraphVisualization import GraphVisualization

##################################################
# Get the data from the files

files = os.listdir('./files/')
if files == []:
	raise Exception("'files' is empty.")

with open("data.json", "w") as f:
	json.dump({}, f)

LayoutManager.get_data(files)

##################################################
# Get statistics

with open('data.json') as file:
	digrams = json.loads(file.read())['digram']
	keys = list(digrams.keys())
	values = list(digrams.values())

	fig = plt.figure(figsize = (10, 5))

	# creating the bar plot
	plt.bar(keys, values)
	plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
	if not os.path.exists('./images'):
		os.mkdir('./images')
	plt.savefig('./images/Histogram.png')
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
