from itertools import zip_longest

name = ['virat', ' rohit', 'ABD']
country = ['IND','IND','SA']
runs = [12000,10000,8000]
ipl = ['RCB','MI']

# plrInfo = list(zip_longest(name, country, runs,ipl))


# print(plrInfo)


#Using Map function

def infogather(name, country, runs,ipl):
   return (name, country, runs,ipl)

plr = map(infogather,name, country, runs,ipl)

print(list(plr))


s={12,23,34,23,45,56}
print(s)

for index,val in enumerate(s):
   print(index,val)