import random
import math

def wallis(n):
 prod=1
 for i in range(1,n+1):
  k=4*math.pow(i,2)
  prod=prod*(k/(k-1))
 pi=2*prod
 return pi

def monte_carlo(n):
 count=0
 for i in range(1,n+1):
  x=random.random()
  y=random.random()
  z=math.pow(x,2)+math.pow(y,2)
  distance=math.sqrt(z)
  if distance<1:
   count+=1

 pi=4*(count/n)
 return pi


  

n=int(input("enter the number of times"))
wallis(n)
monte_carlo(n)

  
   
