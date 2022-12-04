with open("input.txt") as f_obj:
	lines = [line.rstrip() for line in f_obj]

overlap = 0
for line in lines:
	sec1, sec2 = line.split(",")

	start1, end1 = [int(num) for num in sec1.split("-")]
	start2, end2 = [int(num) for num in sec2.split("-")]
	
	# The ranges overlap only if the maximum start
	# value is smaller than or equal to the minimum end value
	if max(start1, start2) <= min(end1, end2):
		overlap += 1
		print(line)

print(overlap)
