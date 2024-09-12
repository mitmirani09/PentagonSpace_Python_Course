class Charger:
   def __init__(self,name):
      self.cname = name
      print("Charger is ready")
   
   def getCharger(self):
      print("Charger is ready to use")

class Mobile:
   def __init__(self,name):
      self.mname = name
      print("Mobile is ready")
      self.c1 =''
   
   def hasMobile(self,c1):
      self.c1 = c1
      print("Mobile is ready to use")
   

c = Charger('Iphone Charger')
m = Mobile('Iphone')
c.getCharger()
m.hasMobile(c)
print(m.c1.cname)
print(m.mname)
del m
print(c.cname)