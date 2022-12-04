import string

f_obj = open("input.txt")

letters = string.ascii_lowercase + string.ascii_uppercase

priorities_sum = 0
for line in f_obj:
	line = line.rstrip()
	mid = len(line) // 2
	first, second = line[:mid], line[mid:]
	
	# Convert halves to sets
	first = set(first)
	second = set(second)
	
	# Get common letter
	common = first.intersection(second).pop()
	
	# Priority of any letter is it's index + 1 in letters
	priorities_sum += letters.find(common) + 1

print(priorities_sum)
f_obj.close()
