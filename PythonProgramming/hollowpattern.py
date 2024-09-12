
n = 4
for i in range(1,n+1):
   for j in range(1,n+1):
      if i == 1 or i == n or j == 1 or j == n:
         print("* ",end="")
      
      else: print("  ",end="")
   print()


n = 5
for i in range(1,n+1):
   for j in range(1,n+1):
      if i == 1 or i == n or j == 1 or j == n or i == j or (i + j) == n+1:
         print("* ",end="")
      
      else: print("  ",end="")
   print()
n = 5
for i in range(1,n+1):
   for j in range(1,n+1):
      if i == 1 or i == n or  i == j or (i + j) == n+1:
         print("* ",end="")
      
      else: print("  ",end="")
   print()


n = 5
for i in range(1,n+1):
   for j in range(1,n+1):
      if j == 1 or j == n or i == j or (i + j) == n+1:
         print("* ",end="")
      
      else: print("  ",end="")
   print()


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
