from collections import deque

with open("input.txt") as f_obj:
	chars = f_obj.readline()

unique_char_num = 14

# Keep only unique_char_num chars in sub_str
sub_str = deque(maxlen = unique_char_num)

for i, char in enumerate(chars, 1):
	sub_str.append(char)
	# Check that required number of characters were added and
	# that all characters in sub_str are unique
	if i >= unique_char_num + 1 and len(set(sub_str)) == unique_char_num:
		print("".join(sub_str))
		break

print(i)
