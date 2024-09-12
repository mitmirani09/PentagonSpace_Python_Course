a= [10, 20, 30, 40]

for i in a:
   print(i)

for index,values in enumerate(a):
   print(index, ":", values)

import copy
# b = [10, 20, 30, 40,[50]]
b1= b


c = copy.deepcopy(b) #deep copy for 2d arrays

b[4][0] = 90
print(b)
print(b1)
print(c)

