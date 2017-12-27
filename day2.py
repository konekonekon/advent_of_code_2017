def checksum(rows):
	# Create generator. Inside of generator, create a list to iterate below.
	# generator is lighter than list
	rows = ([int(r) for r in row.strip().split()] for row in rows)
	# "if row" treats the case where empty line.
	diff = (max(row) - min(row) for row in rows if row)
	# generator can be stored somewhere. So it can be added with sum().
	return sum(diff)


def day2(path):
	with open(path) as f:
		content = f.readlines()
	
	result = checksum(content)
	print(result)


if __name__ == '__main__':
	day2('./day2_input1.d')