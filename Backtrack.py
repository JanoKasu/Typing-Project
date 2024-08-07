import math
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
	sum = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			di = str(matrix[i][j]) + key
			rev = key + str(matrix[i][j])
			if digrams.__contains__(di):
				sum += ((abs(i-row) + abs(j-col)) * digrams[di])
			elif digrams.__contains__(rev):
				sum += ((abs(i-row) + abs(j-col)) * digrams[rev])
			else:
				sum += monograms[key]
	return sum

def Backtrack(matrix, pos):
	if pos == 30:
		return matrix
	i = pos // 10
	j = pos % 10
	file = json.loads(open('data.json', 'r').read())["monogram"]
	for key in file:
		# Remove duplicates
		if get_used(matrix).__contains__(key):
			continue
		# Maximize clusters
		new_matrix = copy.deepcopy(matrix)
		new_matrix[i][j] = key
		value = get_value(new_matrix, i, j)
		prev_value = get_value(matrix, i, j)
		print(new_matrix)
		if value <= prev_value:
			continue
		return Backtrack(new_matrix, pos+1)
	matrix[i][j] = 0


w, h = 10, 3
zeroes = [[0 for x in range(w)] for y in range(h)]
with Halo(text='Loading', spinner='dots'):
	print(Backtrack(zeroes, 0))