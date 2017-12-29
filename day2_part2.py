def check_row(row):
	# pour chaque ligne, trouver le produit cartesian ??

	for r in row:
		for i in range(len(row)):
			if row[i] != r:
				if row[i] % r == 0:
					diviser = row[i] // r
	
	return diviser


def checksum(rows):
	rows = ([int(r) for r in row.strip().split()] for row in rows)
	# diff = (max(row) - min(row) for row in rows if row)


	return sum(check_row(row) for row in rows)

	# for row in rows:

	# 	row.sort()
	# 	for r in row:
	# 		if row[:row.index(r):-1] % r == 0:
	# 			row[:row.index(r):-1] // r
			


	# 	print(row)

	# return sum(diff)
	# return rows


def day2(path):
	with open(path) as f:
		content = f.readlines()
	
	result = checksum(content)
	print(result)


if __name__ == '__main__':
	day2('./day2_input1.d')