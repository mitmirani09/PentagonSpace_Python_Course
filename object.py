
setFan = False
class fan():
   def __init__(self,brand,color,price):
      self.brand = brand
      self.color = color
      self.price = price
      # self.setFan = False
   
   def fanOn(self):
      global setFan
      if setFan == True:
         print("Fan is already rotating")
      else:
         setFan = True
         print("Fan is starting to rotate")
   
   def fanOff(self):
      global setFan
      if setFan == False:
         print("Fan is already off")
      else:
         setFan = False
         print("Fan is turned off")
   
f1 = fan("polycab","white",1000)
print(f1.color)
print(f1.brand)
print(f1.price)

f1.fanOn()
f1.fanOn()
f1.fanOff()
f1.fanOff()



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