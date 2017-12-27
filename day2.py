import sys


def checksum(rows):
	list_difference = []
	total = 0

	rows = [(int(r) for r in row.strip() if r != ("\t" or " ")) for row in rows]
	# diff = [max(row) - min(row) for row in rows]

	for row in rows:
		max_n = -sys.maxsize
		min_n = sys.maxsize
		for r in row:
			print(r)
			if r > max_n:
				max_n = r
			if r < min_n:
				min_n = r

		total += max_n - min_n
		print(max_n, min_n)
		# list_difference.append(diff)

	return total


def day2(path):
	with open(path) as f:
		content = f.readlines()
	
	# print(content)
	result = checksum(content)
	# print(result)


day2('./day2_input.d')