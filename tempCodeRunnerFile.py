class Hero:
   def __init__(self):
      self.name = 'Balayya'
      self.place = 'Hyd'
      self.age = 22

   def dance(self):
      print('Hero is dancing')
   
   def sleep(self):
      print("Hero is sleeping")

h1= Hero()
print(h1.name)
print(h1.place) 
h1.name ='SRK'
h1.place ='Delhi'
# h1.owner ='KKR'
print(h1.name)
print(h1.place)