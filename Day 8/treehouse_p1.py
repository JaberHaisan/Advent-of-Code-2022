with open("input.txt") as f_obj:
	data = []
	for line in f_obj:
		data.append([int(elem) for elem in line.rstrip()])

rows_tot = len(data)
cols_tot = len(data[0])

def is_visible(row, col):
	"""Returns True if tree is visible and otherwise False."""
	tree = data[row][col]
	# Check all trees above current tree.
	for i in range(row - 1, -1, -1):
		if data[i][col] >= tree:
			break
	else:
		return True
	
	# Check all trees below current tree.
	for i in range(row + 1, len(data)):
		if data[i][col] >= tree:
			break
	else:
		return True
		
	# Check all trees to the left of current tree.
	for neighbour in reversed(data[row][:col]):
		if neighbour >= tree:
			break
	else:
		return True
	
	# Check all trees to the right of current tree.
	for neighbour in data[row][col + 1:]:
		if neighbour >= tree:
			break	
	else:
		return True	
	
	return False

# All outer trees are visible
visible_trees = (rows_tot + cols_tot) * 2 - 4

# Check all inner trees
for row in range(1, rows_tot - 1):
	for col in range(1, cols_tot - 1):
		if is_visible(row, col):
			visible_trees += 1

print(visible_trees)
