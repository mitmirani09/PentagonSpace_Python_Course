class Car:
   def __init__(self,name):
      self.cname = name
      print('car is ready')

   def getCar(self):
      print('Car is ready to drive')

class Heart:
   def __init__(self,name):
      self.hname = name
      print('Our heart is ready')

   def getHeart(self):
      print('Heart is ready to beat')


class Person:
   def __init__(self,name):
      self.pname = name
      self.h = Heart("love") #Composed
      self.c1 = ''  #Aggregated
      print('Our person is ready to jog')
   
   def hasPerson(self,c):
      self.c1 = c
      print('Person and Heart connected')

p = Person('Mit')
c = Car('Porsche GT')
p.hasPerson(c)
print(p.pname)
print(p.h.hname)
print(p.c1.cname)
