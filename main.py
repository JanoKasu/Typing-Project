import layoutManager
from collections import defaultdict
from GraphVisualization import GraphVisualization
import json
# import Alg

PDFs = ['The Grammar of English Grammars.pdf', 'Chubby--Charming.pdf', 'Harry Potter and the Cursed Child.pdf', 'The Book Thief.pdf', 'The Hitchhikers Guide to the Galaxy.pdf', 'The Last Crusade.pdf', 'A Thousand Plateaus.pdf', 'The Hunger Games.pdf', 'The Kite Runner.pdf']

##################################################
# Clear the JSON file
with open("data.json", "w") as f:
	json.dump("{}", f)

layoutManager.getGraph(PDFs)

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