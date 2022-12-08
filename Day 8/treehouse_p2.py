with open("input.txt") as f_obj:
	data = []
	for line in f_obj:
		data.append([int(elem) for elem in line.rstrip()])

rows_tot = len(data)
cols_tot = len(data[0])

def scenic_score(row, col):
	"""Returns scenic score of Tree."""
	tree = data[row][col]
	up, down, left, right = [0, 0, 0, 0]
	
	# Check trees above current tree.
	for i in range(row - 1, -1, -1):
		up += 1
		if data[i][col] >= tree:
			break
	
	# Check trees below current tree.
	for i in range(row + 1, len(data)):
		down += 1
		if data[i][col] >= tree:
			break
		
	# Check trees to the left of current tree.
	for neighbour in reversed(data[row][:col]):
		left += 1
		if neighbour >= tree:
			break
	
	# Check trees to the right of current tree.
	for neighbour in data[row][col + 1:]:
		right += 1
		if neighbour >= tree:
			break	
	
	return up * down * right * left

max_score = 0
# Check all inner trees. Scores for outer trees are already 0 so can 
# never be maximum.
for row in range(1, rows_tot - 1):
	for col in range(1, cols_tot - 1):
		score = scenic_score(row, col)
		if score > max_score:
			max_score = score

print(max_score)
