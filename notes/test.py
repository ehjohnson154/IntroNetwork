
bleh = "file2.html"

def open_file(filename):
	try:
		with open(filename) as fp:
			data = fp.read()   # Read entire file
			return data

	except:
		# File not found or other error
		print("no")


stuff = open_file(bleh)
print(stuff)
print(type(stuff))