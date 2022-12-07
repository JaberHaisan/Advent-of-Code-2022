from collections import deque

with open("input.txt") as f_obj:
	lines = deque(line.rstrip() for line in f_obj.readlines())

class Directory():
	
	def __init__(self, path):
		"""Initialize Directory Class."""
		self.path = path
		self.contents = []
	
	def __repr__(self):
		"""Returns string representation of Directory object."""
		return f"Directory(path={self.path}, contents={self.contents})"
	
	def get_size(self):
		"""Returns the size of contents of Directory."""
		size = 0
		for content in self.contents:
			size += content.get_size()
		return size
		
	def append(self, content):
		"""Adds directory or file to contents."""
		self.contents.append(content)

class File():
	
	def __init__(self, path, size):
		"""Initializes File Class."""
		self.path = path
		self.size = size

	def __repr__(self):
		"""Returns string representation of Directory object."""
		return f"File(path={self.path}, size={self.size})"
		
	def get_size(self):
		"""Returns the size of the file."""
		return self.size

directories = {}
curr_path = ""

while len(lines) != 0:
	line = lines.popleft()
	
	# Move to home directory
	if line == "$ cd /":
		curr_path = "/"
		if curr_path not in directories:
			directories[curr_path] = Directory(curr_path)
		continue
	
	elif line == "$ ls" and len(lines) >= 1:
		line = lines.popleft()
		directory = directories[curr_path]

		while True:
			line = line.split()
			path = curr_path + "/" if curr_path != "/" else curr_path
			
			# Is a directory
			if line[0] == "dir":
				path += line[1]
				
				if path not in directories:
					directories[path] = Directory(path)
					
				directory.append(directories[path])
				
			# Is a file
			else:
				path += line[1]
				file_obj = File(path, int(line[0]))
				directory.append(file_obj)
			
			# If there are more lines and the next line is not a command,
			# pop the next line. Otherwise break out of loop.
			if len(lines) != 0 and not lines[0].startswith("$"):
				line = lines.popleft()
			else:
				break
		
	
	elif line == "$ cd ..":
		# Cannot go further back if already at home directory
		if curr_path == "/":
			continue
		else:
			curr_path = curr_path.split("/")
			# Move up one directory by removing the last directory from current path
			curr_path = "/".join(curr_path[:-1])
	
	# Changing to other directories
	elif line.startswith("$ cd"):
		line = line.split()
		
		if curr_path == "/":
			curr_path += line[2]
		else:
			curr_path += "/" + line[2]
			
		if curr_path not in directories:
			directories[curr_path] = Directory(curr_path)

# Part 1
total = 0
# Get sum of sizes of all directories smaller than 100000
for path, directory in directories.items():
	if path != "/":
		size = directory.get_size()
		if size <= 100000:
			total += size

print("Part 1:", total)

# Part 2
total_disk_size = 70000000
req_free_space = 30000000
occupied_space = directories["/"].get_size()
current_free_space = total_disk_size - occupied_space

# Find all directories whose deletion will free the required amount of space
matching_directory_sizes = []
for path, directory in directories.items():
	if path != "/":
		size = directory.get_size()
		if current_free_space + size >= req_free_space:
			matching_directory_sizes.append(size)

# The smallest directory size is the required answer
print("Part 2:", min(matching_directory_sizes))
