with open("input.txt") as f_obj:
	lines = [line.rstrip() for line in f_obj.readlines()]

X = 1
cycles = 0
pixels = list("." * 40 * 6)

def update_pixels(X, cycles, pixels):
	"""Draws pixels if the sprite's horizontal position (X) puts its pixels
	where the CRT is currently drawing."""
	pos = (cycles - 1) % 40
	if pos in {X-1, X, X+1}:
		pixels[cycles - 1] = "#"
		
for line in lines:
	line = line.split()
	
	if line[0] == "noop":
		cycles += 1
		update_pixels(X, cycles, pixels)
		
	elif line[0] == "addx":
		cycles += 1
		update_pixels(X, cycles, pixels)
		
		cycles += 1
		update_pixels(X, cycles, pixels)			
		X += int(line[1])
			

for i in range(0, 201, 40):
	print("".join(pixels[i: i + 40]))
