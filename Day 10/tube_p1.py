with open("input.txt") as f_obj:
	lines = [line.rstrip() for line in f_obj.readlines()]

X = 1
cycles = 0
signal_strengths = {}

for line in lines:
	line = line.split()
	
	if line[0] == "noop":
		cycles += 1
		signal_strengths[cycles] = X * cycles
		
	elif line[0] == "addx":
		cycles += 1
		signal_strengths[cycles] = X * cycles
		
		cycles += 1
		signal_strengths[cycles] = X * cycles
		X += int(line[1])
	

req_sum = sum(signal_strengths.get(i, 0) for i in range(20, 221, 40))
print(req_sum)
