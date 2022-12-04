f_obj = open("input.txt")

opp_move_codes = {"A": "Rock", "B": "Paper", "C": "Scissors"}
my_move_codes = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
move_points = {"Rock": 1, "Paper": 2, "Scissors": 3}

points_total = 0

for line in f_obj:
	opp_move, my_move = line.rstrip().split()
	opp_move = opp_move_codes[opp_move]
	my_move = my_move_codes[my_move]
	
	points_total += move_points[my_move]
	
	round_moves = {opp_move, my_move} 

	# Draw
	if len(round_moves) == 1:
		points_total += 3
		
	# Rock/Paper
	elif round_moves == {"Paper", "Rock"}:
		# Win
		if my_move == "Paper":
			points_total += 6
		# Lose
		else:
			points_total += 0
	
	# Rock/Scissors
	elif round_moves == {"Scissors", "Rock"}:
		# Win
		if my_move == "Rock":
			points_total += 6
		# Lose
		else:
			points_total += 0		
			
	# Paper/Scissors
	elif round_moves == {"Paper", "Scissors"}:
		# Win
		if my_move == "Scissors":
			points_total += 6
		# Lose
		else:
			points_total += 0		

print(points_total)

f_obj.close()
