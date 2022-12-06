from collections import deque

with open("input.txt") as f_obj:
	lines = [line.rstrip() for line in f_obj]

# space_pos contains the location of the space between stacks
# and moves in the input text.
space_pos = lines.index("") + 1

stack_strings, moves = lines[:space_pos - 1], lines[space_pos:]

# Get total number of stacks through manipulating the line with the number
# of stacks
stacks_num = stack_strings[-1].split()[-1]
stacks_num = int(stacks_num)

# Remove last line with number of stacks since it is no longer needed
stack_strings = stack_strings[:-1]

# Convert stack_strings to a list of deques
stacks = [deque() for i in range(stacks_num)]
for stack_string in stack_strings:
	index = 1
	curr_stack = 0
	while index < len(stack_string):
		if stack_string[index].isalpha():
			stacks[curr_stack].append(stack_string[index])
		index += 4
		curr_stack += 1
			
# Perform one move at a time
for move in moves:
	move = move.split()
	_, num, _, source, _, dest = move
	
	num = int(num)
	# Index of stacks need to be adjusted by 1
	source = int(source) - 1
	dest = int(dest) - 1
	
	# Move num items from source stack to dest stack
	items = deque()
	for i in range(num):
		item = stacks[source].popleft()
		items.appendleft(item)
	stacks[dest].extendleft(items)

# Create the required string
res_str = ""
for stack in stacks:
	if len(stack) != 0:
		res_str += stack[0]

print(res_str)
