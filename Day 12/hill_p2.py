import string
from collections import deque

with open("input.txt") as f_obj:
	lines = [line.rstrip() for line in f_obj.readlines()]

class Node():
	
	def __init__(self, letter, row, col):
		"""Initialize node class."""
		self.letter = letter
		self.row = row
		self.col = col
		
		self.predec = None
		self.distance = float("inf")
		self.neighbours = []

	def __repr__(self):
		"""Return repr(self)."""
		return f"Node({self.letter}, row={self.row}, col={self.col})"
	
	def add_neighbour(self, other):
		"""Adds other to neighours of node."""
		self.neighbours.append(other)
	
	def reset(self):
		"""Resets predec and distance."""
		self.predec = None
		self.distance = float("inf")
		
nodes = {}
starts = []

# Create nodes from data
for row, line in enumerate(lines):
	for col, letter in enumerate(line):
		if letter == "S" or letter == "a":
			start = Node("a", row, col)
			nodes[(row, col)] = start
			starts.append(start)
			
		elif letter == "E":
			end = Node("z", row, col)
			nodes[(row, col)] = end
			
		else:
			nodes[(row, col)] = Node(letter, row, col)

letters = string.ascii_lowercase

# x and y are letters. The function checks their pos in letters
# and returns true if pos(y) is below or equal to pos(x + 1)
comp_letters = lambda x, y: letters.find(y) <= letters.find(x) + 1

# Determine neigbours of each node
for (row, col), node in nodes.items():
	# Up
	if (row + 1, col) in nodes and comp_letters(node.letter, nodes[(row + 1, col)].letter):
		node.add_neighbour(nodes[(row + 1, col)])
	# Down
	if (row - 1, col) in nodes and comp_letters(node.letter, nodes[(row - 1, col)].letter):
		node.add_neighbour(nodes[(row - 1, col)])	
	# Left
	if (row, col - 1) in nodes and comp_letters(node.letter, nodes[(row, col - 1)].letter):
		node.add_neighbour(nodes[(row, col - 1)])
	# Right
	if (row, col + 1) in nodes and comp_letters(node.letter, nodes[(row, col + 1)].letter):
		node.add_neighbour(nodes[(row, col + 1)])

min_distance = float("inf")
for start in starts:
	# Use BFS to find shortest distance
	Q = deque()
	start.distance = 0
	Q.append(start)

	while len(Q) != 0:
		u = Q.popleft()
		for neighbour in u.neighbours:
			# Undiscovered node
			if neighbour.distance == float("inf"):
				neighbour.distance = u.distance + 1
				neighbour.predec = u
				Q.append(neighbour)
			
	min_distance = min(min_distance, end.distance)
	
	# Reset all nodes for next BFS
	for node in nodes.values():
		node.reset()
		
print(min_distance)