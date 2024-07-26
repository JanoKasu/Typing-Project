import random
import Reader
import json
from halo import Halo
from collections import defaultdict
from GraphVisualization import GraphVisualization

def getGraph(PDFs):
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
    
    # Spinning Loader
    # 
    with Halo(text='Loading', spinner='dots'):
        for i in range(len(PDFs)):
            print('\nReading: ' + PDFs[i])
            path = ('PDFs/' + PDFs[i])
            Reader.readPDF(path)


    ##################################################
    # Use the data as a graph, where the frequency of digrams are weights

    # Given a digram, parse the left (start) and right (end) elements
    # Weight is the digram's frequency

    with open('data.json') as file:
        data = json.load(file)
        digram = data['digram']
        for di in digram:
            start = di[0]
            end = di[1]
            weight = digram[di]
            if (start != end):
                addEdge(start, end, weight, graph)

    with open("graph.json", "w") as outfile:
        json.dump(graph, outfile, indent=4, sort_keys=True)

    with open("graph.json", "r") as f:
        G = GraphVisualization()
        data = json.load(f)
        # start is the element in the dictionary that points to a list of other elements
        for start in data:
            # end is the list of elements that start points to
            for end in data.get(start):
                # end[0] is  the letter, end[1] is the weight
                G.addEdge(start, end[0], end[1])
        G.visualize()