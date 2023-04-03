a={'hai','hello','hey'}
b={'hai','how','what','where'}
c={'hai'}
d={'where'}
e={'wherever'}

# union
print(a.union(b))
print(a.union(b)==b.union(a))

# intersection
print(a.intersection(b))
print(a.intersection(b)==b.intersection(a))

# difference
print(a.difference(b))
print(a.difference(b)==b.difference(a))

print(a.symmetric_difference(b))
print(a.symmetric_difference(b)==b.symmetric_difference(a))

# subset
print(d.issubset(b))
print(b.issubset(d))

# superset
print(d.issuperset(b))
print(b.issuperset(d))

# disjoints
print(d.isdisjoint(e))
print(b.isdisjoint(c))