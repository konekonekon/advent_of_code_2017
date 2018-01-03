class MultiSet():
	def __init__(self):
		self.data = {}

	def add(self,v):
		if v in self.data:
			self.data[v] += 1
		if v not in self.data:
			self.data[v] = 1

	def remove(self,v):
		if v in self.data:
			self.data[v] -= 1

	def multiplicity(self, elem):
		if elem in self.data:
			return self.data[elem]
