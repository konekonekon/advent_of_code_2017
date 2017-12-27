def checksum(rows):
	rows = ([int(r) for r in row.strip().split()] for row in rows)
	diff = (max(row) - min(row) for row in rows if row)
	return sum(diff)


def day2(path):
	with open(path) as f:
		content = f.readlines()
	
	result = checksum(content)
	print(result)


if __name__ == '__main__':
	day2('./day2_input1.d')