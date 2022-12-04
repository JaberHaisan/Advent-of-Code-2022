f_obj = open("input.txt")

opp_move_codes = {"A": "Rock", "B": "Paper", "C": "Scissors"}
move_points = {"Rock": 1, "Paper": 2, "Scissors": 3}

lose_moves = {"Paper": "Rock", "Scissors": "Paper", "Rock": "Scissors"}
win_moves = {val: key for key, val in lose_moves.items()}

points_total = 0

for line in f_obj:
	opp_move, round_type = line.rstrip().split()
	opp_move = opp_move_codes[opp_move]

	# Lose
	if round_type == "X":
		my_move = lose_moves[opp_move]
		points_total += move_points[my_move]
		points_total += 0
		
	# Draw
	elif round_type == "Y":
		points_total += move_points[opp_move]
		points_total += 3
	
	# Win
	elif round_type == "Z":
		my_move = win_moves[opp_move]
		points_total += move_points[my_move]
		points_total += 6

print(points_total)

f_obj.close()
