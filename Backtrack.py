import copy
import json
import math
from threading import Thread
from alive_progress import alive_bar

def get_used(matrix):
	used = []
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] != 0:
				used.append(matrix[i][j])
	return used


def get_value(matrix):
	digrams = json.loads(open('data.json', 'r').read())["digram"]
	
	sum = 0
	for column in range(len(matrix[0])):
		for i in range(2):
			verticalScore = 0
			di = str(matrix[i][column] + matrix[i-1][column])
			rev = str(matrix[i-1][column] + matrix[i][column])
			if di in digrams:
				verticalScore += digrams[di]
			elif rev in digrams:
				verticalScore += digrams[rev]
			else:
				verticalScore += 0
		sum += verticalScore
	return sum
			

def backtrack(bestMatrix, matrix, pos):
	if pos >= 30:
		if get_value(matrix) > get_value(bestMatrix):
			bestMatrix = matrix
		bar()
		return bestMatrix
	
	i = pos // 10
	j = pos % 10
	file = json.loads(open('data.json', 'r').read())["monogram"]
	new_matrix = copy.deepcopy(matrix)
	used = get_used(matrix)

	for key in file:
		# Remove duplicates
		if key not in used:
			new_matrix[i][j] = key
			backtrack(bestMatrix, new_matrix, pos+1)
	matrix[i][j] = 0


w, h = 10, 3
zeroes = [[0 for x in range(w)] for y in range(h)]
bestMatrix = copy.deepcopy(zeroes)
monograms = json.loads(open('data.json', 'r').read())["monogram"]
with alive_bar(math.factorial(30)) as bar:
	threads = list()
	for letter in monograms:
		temp = copy.deepcopy(zeroes)
		temp[0][0] = letter
		thread = Thread(target=backtrack, args=(bestMatrix, temp, 1))
		threads.append(thread)
		thread.start()
	for thread in threads:
		thread.join()
	print(bestMatrix)