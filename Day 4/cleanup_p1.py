with open("input.txt") as f_obj:
	lines = [line.rstrip() for line in f_obj]

fully_contained = 0
for line in lines:
	sec1, sec2 = line.split(",")

	sec1 = [int(num) for num in sec1.split("-")]
	sec2 = [int(num) for num in sec2.split("-")]
	
	# Section 2 is fully contained by Section 1
	overlap_sec1 = (sec1[0] <= sec2[0] <= sec1[1]) and (sec1[0] <= sec2[1] <= sec1[1])
	
	# Section 1 is fully contained by Section 2
	overlap_sec2 = (sec2[0] <= sec1[0] <= sec2[1]) and (sec2[0] <= sec1[1] <= sec2[1])
	
	if overlap_sec1 or overlap_sec2:
		fully_contained += 1

print(fully_contained)
