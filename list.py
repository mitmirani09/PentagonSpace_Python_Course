l = []

while True:
   data = int(input('Enter data'))
   l.append(data)
   print("press 1 to add another data or 2 to end")
   choice = int(input())
   if choice == 1:
      continue
   else:
      break

print(l)
print(type(l))
print(len(l))
print(l[1])
l[0] = 200
print(l)