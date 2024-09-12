n = 6
noc,nor = n,n
for i in range(1,n*2):
   for j in range(1,n*2):
      if j == noc or j == nor:
         print("*",end="")
      else:print(" ",end='')
   print()
   if i<n:
      noc -= 1
      nor += 1
   else:
      noc += 1
      nor -= 1