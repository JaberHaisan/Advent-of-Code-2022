import string

letters = string.ascii_lowercase + string.ascii_uppercase

with open("input.txt") as f_obj:
	data = [line.rstrip() for line in f_obj]

priorities_sum = 0
for i in range(0, len(data), 3):
	gr1, gr2, gr3 = data[i: i + 3]
	gr1 = set(gr1); gr2 = set(gr2); gr3 = set(gr3)
	
	# Get common letter
	common = gr1.intersection(gr2.intersection(gr3)).pop()

	# Priority of any letter is it's index + 1 in letters
	priorities_sum += letters.find(common) + 1

print(priorities_sum)
