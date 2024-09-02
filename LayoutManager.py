import Reader
import json
from halo import Halo
from collections import defaultdict

##################################################
# function for adding edge to graph 
def add_edge(start, end, weight, graph):
    if (graph[start] != None):
        graph[start].append([end, weight])
    else:
        graph[start] = [end, weight]

##################################################
# Main function
def get_data(files):
    with open("data.json", "w") as f:
        json.dump("{}", f)
         
    
    graph = defaultdict(list)
    # Spinning Loader
    with Halo(text='Loading', spinner='dots'):
        # Read each PDF
        for i in range(len(files)):
            print('\nReading: ', files[i])
            path = ('files/' + files[i])
            if files[i].endswith('.pdf'):
                Reader.read_pdf(path)
            elif files[i].endswith('.txt'):
                Reader.read_txt(path)
            else:
                continue

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
                add_edge(start, end, weight, graph)

    with open("graph.json", "w") as f:
	    json.dump(graph, f, indent=4, sort_keys=True)
