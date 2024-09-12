class Cargo:
   def takeOn(self):
      print("Plane takes on")
   
   def takeOff(self):
      print("Plane takes off")
   
   def land(self):
      print("Plane landing")

   def carry(self):
      print("Plane carrying cargo's in it.")


class Passenger:
   def takeOn(self):
      print("Plane takes on")

   def takeOff(self):
      print("Plane takes off")
   
   def land(self):
      print("Plane landing")

   def carry(self):
      print("Plane carrying passenger's in it.")


class Fighter:
   def takeOn(self):
      print("Plane takes on")

   def takeOff(self):
      print("Plane takes off")
   
   def land(self):
      print("Plane landing")
   
   def carry(self):
      print("Plane carrying weapon's in it.")

c1 = Cargo()
p1 = Passenger()
f1 = Fighter()

c1.takeOn()
c1.takeOff()
c1.land()32
c1.carry()

(p1.takeOn())
(p1.takeOff())
(p1.land())
(p1.carry())

(f1.takeOn())
(f1.takeOff())
(f1.land())
(f1.carry())

