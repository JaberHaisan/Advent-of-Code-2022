f_obj = open("input.txt")

food_totals = []
curr_food = 0
for line in f_obj:
	if line == '\n':
		food_totals.append(curr_food)
		curr_food = 0
	else:
		food = int(line.rstrip())
		curr_food += food

food_totals.sort(reverse = True)
print(sum(food_totals[:3]))
