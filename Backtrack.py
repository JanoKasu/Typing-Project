import copy
import json
from halo import Halo

def get_used(matrix):
	used = []
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] != 0:
				used.append(matrix[i][j])
	return used

def get_value(matrix, row, col):
	monograms = json.loads(open('data.json', 'r').read())["monogram"]
	digrams = json.loads(open('data.json', 'r').read())["digram"]
	key = matrix[row][col]
	if key == 0:
		return 0
	if row + col == 0:
		return monograms[key]
	di = str(matrix[row][col-1]) + key
	rev = key + str(matrix[row][col-1])
	if di in digrams:
		return monograms[key] / digrams[di]
	elif rev in digrams:
		return monograms[key] / digrams[rev]
	else:
		return monograms[key]

def backtrack(matrix, pos):
	if pos >= 30:
		return matrix
	
	i = pos // 10
	j = pos % 10
	file = json.loads(open('data.json', 'r').read())["monogram"]
	new_matrix = copy.deepcopy(matrix)
	
	for key in file:
		new_matrix[i][j] = key
		value = getValue(new_matrix, i, j)
		prev_value = getValue(matrix, i, j)
		
		# Remove duplicates
		if key in getUsed(matrix):
			continue
		# Maximize clusters
		elif value <= prev_value:
			continue
		# Backtrack for the next position
		else:
			print(new_matrix)
			backtrack(new_matrix, pos+1)
	matrix[i][j] = 0


w, h = 10, 3
zeroes = [[0 for x in range(w)] for y in range(h)]
with Halo(text='Loading', spinner='dots'):
	print(backtrack(zeroes, 0))