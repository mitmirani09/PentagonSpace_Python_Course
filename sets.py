s= set()
for i in range(5):
   data = int(input())
   s.add(data)
print(s)

s.update([60,70,80])
print(s)
s.remove(60)
s.discard(70)
s.discard(900)
print(s)
try:
   s.remove(800)
except Exception as e:
   print(e)
print(s)


s1={1,2,3,4,5}
s2={3,4,5,6}
print(s1)
print(s2)

s3 = s1.union(s2)
print(s3)

s4 = s1.intersection(s2)
print(s4)

s5 = s1.difference(s2)
print(s5)
s6 = s1.symmetric_difference(s2)
print(s6)
