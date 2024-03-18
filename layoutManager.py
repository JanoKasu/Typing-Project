import Reader
import json
from halo import Halo
from collections import defaultdict
from GraphVisualization import GraphVisualization

graph = defaultdict(list)

##################################################
# function for adding edge to graph 

def addEdge(start, end, weight, graph):
    if (graph[start] != None):
        graph[start].append([end, weight])
    else:
        graph[start] = [end, weight]

##################################################
# Main function

PDFs = ['The Grammar of English Grammars.pdf', 'Chubby--Charming.pdf', 'Harry Potter and the Cursed Child.pdf', 'The Book Thief.pdf', 'The Hitchhikers Guide to the Galaxy.pdf', 'The Last Crusade.pdf']
test = ['meetingminutes.pdf']

# Change test to PDFs when ready to run
with Halo(text='Loading', spinner='dots'):
    for i in range(len(test)):
        print('\nReading: ' + test[i])
        pdf = open('PDFs/' + test[i], 'rb')
        Reader.readPDForTxt(pdf)


##################################################
# Use the data as a graph, where the digrams are edges

# Given a digram, parse the left (start) and right (end) elements
# Weight is the digram's value

with open('data.json') as f:
    data = json.load(f)
    digram = data['digram']
    for di in digram:
        start = di[0]
        end = di[1]
        weight = digram[di]
        if (start != end):
            addEdge(start, end, weight, graph)

    

with open("graph.json", "w") as outfile:
    json.dump(graph, outfile, indent=4, sort_keys=True )


with open("graph.json", "r") as f:
    G = GraphVisualization()
    data = json.load(f)
    print(data)
    # start is the element in the dictionary that points to a list of other elements
    for start in data:
        # end is the list of elements that start points to
        for end in data.get(start):
            # end[0] is  the letter, end[1] is the weight
            G.addEdge(start, end[0], end[1])
    G.visualize()
