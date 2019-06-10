l1 = [1,3,2,4,5]
print (l1)
l1.reverse()
print (l1)
l1.sort()
print (l1)

l2 = reversed(l1)
print (list(l2))
l3 = sorted(l1, reverse=True)
print (l3)

print (l3.__sizeof__())
