import random
import sys
import json
from operator import itemgetter

def minimize():
    # Minimize total r value
    # distance is lower for better candidate positions
    # weight is lower for poorly related letters
    with open("distance.json", "r") as distance, open("data.json", "r") as data:
        dist = json.load(distance)
        weight = json.load(data)["monogram"]
        used = []
        result = []

        for letter in reversed(weight):
            bestheur = sys.maxsize
            bestpos = -1
            for pos in dist:
                # Calculate heuristic
                heur = dist[pos]*weight[letter]
                if (heur < bestheur and not used.__contains__(pos)):
                    bestheur = heur
                    bestpos = pos
            used.append(bestpos)
            result.append({letter : bestpos})
            
minimize()