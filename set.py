"""s={1,2,5}
print(s)
print(type(s))

s.add(20)
print(s)
s.remove(1)
print(s)
s.pop()
print(s)
s.add(1)
print(s)"""

#frozenset
s={1,3,7,9}
s1=frozenset(s)
print(s1)
print(type(s1))
for i in s1:
    print(i)
