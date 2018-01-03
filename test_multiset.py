import multi_set

m = multi_set.MultiSet()
m.add(1)
m.add(2)
m.add(1)
m.add(3)
m.add(2)

print(m.multiplicity(2))
m.remove(2)
print(m.multiplicity(2))