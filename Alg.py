import copy
import math
import json
from halo import Halo

# First prioritize the home row
# Then prioritize low distances from the center
def get_dist(matrix):
	digrams = json.loads(open('data.json', 'r').read())["digram"]
	dist = json.loads(open('distance.json', 'r').read())
	sum = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == 0:
				continue
			for k in range(len(matrix)):
				for l in range(len(matrix[k])):
					if matrix[k][l] == 0:
						continue
					di = matrix[i][j] + matrix[k][l]
					rev = matrix[k][l] + matrix[i][j]
					if digrams.__contains__(di):
						sum = ((abs(i-k) + abs(j-l)) * digrams[di]) / (dist[str(i+j)] + dist[str(k+l)])
					elif digrams.__contains__(rev):
						sum = ((abs(i-k) + abs(j-l)) * digrams[rev]) / (dist[str(i+j)] + dist[str(k+l)])
					else:
						continue
	return sum

def get_used(matrix):
	used = []
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] != 0 and not matrix.__contains__(matrix[i][j]):
				used.append(matrix[i][j])
	print("used: ", used)
	return used

def Alg(matrix, i, j):
	file = json.loads(open('data.json', 'r').read())["monogram"]
	while i < len(matrix) and j < len(matrix[i]):
		for key in file:
			used = get_used(matrix)
			if used.__contains__(key):
				print("key: ", key, " is used")
				continue
			newMatrix = copy.deepcopy(matrix)
			newMatrix[i][j] = key
			if get_dist(newMatrix) < get_dist(matrix):
				print("key: ", key, "new < old")
				continue
			print("newMatrix: ", newMatrix)
		j += 1
		i += j // 10
		j = j % 10
		print("i: ", i, " j: ", j)
		Alg(matrix, i, j)
	return matrix


w, h = 10, 3
zeroes = [[0 for x in range(w)] for y in range(h)]
with Halo(text='Loading', spinner='dots'):
	print(Alg(zeroes, 0, 0))