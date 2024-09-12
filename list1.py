lis = [1,2,3,[10,20,30,[100,200,300]]]

print(lis[1])
print(lis[3][1])
print(lis[3][3][1])


# Operations on lists:

a = [1,2,3]
b = [1,2,3]


print(a+b)
print(a*2)
print(90 in a)
print( 2 in a)
print(a in b)



#print(a*b)


#Copy methods

a = [40,10,5,20,50]
a1 = a #Shallow copy
b = a.copy() #Deep copy
# a[2] = 90
print(a1)
print(a)
print(b)
b[2] = 99
print(b)
print(a)


print(max(a))
print(min(a))
print(sorted(a))
# print(sorted(a, reverse=True))
a.reverse()
print(a)


a=[10,20,30]
print(len(a))
a.insert(1,25)
print(a)

a.append(40)
print(a)

b=[50,60,70]
a.append(b)
print(a)
a.extend(b)
print(a)