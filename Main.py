import time
import random as rand

space = ' '
segundos = 0.07

for i in range(10000):
   y, z = rand.randint(3,19), rand.randint(3,15)
   a, b = rand.randint(3,18), rand.randint(3,15)
   b1, b2= rand.randint(0,1), rand.randint(0,1)
   
   print(space*z,b1,space*y,b2,space*a,b1,space*b,b1)
   time.sleep(segundos)