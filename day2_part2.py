def check_row(row):
	# return ((row[i]//r for i in range(len(row)) if row[i]!=r if row[i]%r==0) for r in row)

	for r in row:
		for i in range(len(row)):
			if row[i] != r:
				if row[i] % r == 0:
					diviser = row[i] // r
	
	return diviser


def checksum(rows):
	rows = ([int(r) for r in row.strip().split()] for row in rows)
	return sum(check_row(row) for row in rows)


def day2(path):
	with open(path) as f:
		content = f.readlines()
	
	result = checksum(content)
	print(result)


if __name__ == '__main__':
	day2('./day2_input.d')