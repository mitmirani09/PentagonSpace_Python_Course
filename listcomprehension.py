l = [10, 20, 30, 40]
b=[]

for i in l:
   data = i + 1
   b.append(data)

print(b)


#converting the above code to list comprehension

c=[data+1 for data in l]
print(c)
