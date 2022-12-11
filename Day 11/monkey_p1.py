import operator
from dataclasses import dataclass
from math import lcm

all_monkey_desc = []
with open("test.txt") as f_obj:
	lines = [line.rstrip() for line in f_obj.readlines()]
	
	# Separate lines to lists of description of each monkey
	for i in range(0, len(lines), 7):
		all_monkey_desc.append(lines[i:i + 6])

@dataclass
class Monkey():
	name: str = None
	items: list = None
	op: str = None
	operand: str = None
	divisor: int = None
	monk1: str = None
	monk2: str = None
	inspect: int = 0
		
	def turn(self, monkeys, modulus):
		"""Checks worry levels for every item and gives item 
		to another monkey according to test."""
		for old in self.items:
			# Calculate new worry level
			new = ops[self.op](old, eval(self.operand))
			new //= 3
			new %= modulus
			
			# Give item over to a different monkey
			if new % self.divisor == 0:
				monkeys[self.monk1].take(new)
			else:
				monkeys[self.monk2].take(new)
			
			self.inspect += 1
			
		# All items passed over to other monkeys
		self.items.clear()
		
	def take(self, item):
		"""Adds an item to items."""
		self.items.append(item)

ops = { "+": operator.add, "*": operator.mul}

monkeys = {}
for monkey_desc in all_monkey_desc:
	monkey = Monkey()
	
	# Extra data from each line
	for i, line in enumerate(monkey_desc):
		line = line.split()

		if i == 0:
			monkey.name = line[1].replace(":", "")
			
		elif i == 1:
			line = line[2:]
			monkey.items = [int(item.replace(",", "")) for item in line]
			
		elif i == 2:
			op, operand = line[-2:]
			monkey.op = op
			monkey.operand = operand
		
		elif i == 3:
			monkey.divisor = int(line[-1:][0])
			
		elif i == 4:
			monkey.monk1 = line[-1:][0]
			
		elif i == 5:
			monkey.monk2 = line[-1:][0]
	
	monkeys[monkey.name] = monkey

modulus = lcm(*[monkey.divisor for monkey in monkeys.values()])
rounds = 20
for i in range(rounds):
	for monkey in monkeys.values():
		monkey.turn(monkeys, modulus)

# Sort monkeys according to their number of inspections.
monkeys = sorted(monkeys.items(), key = lambda item: item[1].inspect, reverse = True)

monkey_business = monkeys[0][1].inspect * monkeys[1][1].inspect
print(monkey_business)
