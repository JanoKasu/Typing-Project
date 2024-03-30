import random
import json
from operator import itemgetter

def minimize():
    # Minimize total r value
    # distance is lower for better candidate positions
    # weight is lower for poorly related letters
    with open("distance.json", "r") as f1, open("data.json", "r") as f2:
        dist = json.load(f1)
        weight = json.load(f2)["monogram"]
        used = []
        result = []

        for letter in reversed(weight):
            bestheur = 10000000000
            bestpos = -1
            for pos in dist:
                # Calculate heuristic
                heur = dist[pos]*weight[letter]
                if (heur < bestheur and not used.__contains__(pos)):
                    bestheur = heur
                    bestpos = pos
            used.append(bestpos)
            result.append({letter : bestpos})
        
        print(result)

            
minimize()