#!/usr/bin/python
import random
import sys
g1=0
g2=0
def rozgrywka():
  global g1
  global g2
  taliakart=[]
  gracz1=[]
  gracz2=[]
  
  for numer in range(2,15):
      for kolor in range(0,4):
          taliakart.append(numer)
  taliakart.append(15) # 2 jokery
  taliakart.append(15)
  taliakart.append(15)
  taliakart.append(15)
  
  for x in range(1,1000):
      random.shuffle(taliakart)
  
  for x in range(0,len(taliakart)/2):
      gracz1.append(taliakart[x*2])
      gracz2.append(taliakart[x*2+1])
  
  iteracja=0
  
  while (len(gracz1)>0) and (len(gracz2)>0):
      iteracja+=1
#      if(len(gracz1)>len(gracz2)):
#              print "gracz 1 prowadzi"
#      else:
#              print "gracz 2 prowadzi"
#      print "gracz1: ",gracz1
#      print "gracz2: ",gracz2
      z=[]
      if gracz1[0] > gracz2[0]:
          z.append(gracz1.pop(0))
          z.append(gracz2.pop(0))
          gracz1.extend(z)
      elif gracz1[0]< gracz2[0]:
          z.append(gracz2.pop(0))
          z.append(gracz1.pop(0))
          gracz2.extend(z)
      elif gracz1[0] == gracz2[0] and len(gracz1)>1 and len(gracz2)>1:
#          print("Wojna")
          z.append(gracz1.pop(0))
          z.append(gracz2.pop(0))
          z.append(gracz1.pop(0))
          z.append(gracz2.pop(0))
      else:
          gracz1.append(gracz1.pop(0))
          gracz2.append(gracz2.pop(0))
      if(iteracja>500):
          print gracz1
          print gracz2
          sys.exit(0)

  if (len(gracz1)>0):
      print("Gracz 1 wygral")
      g1+=1
  else:
      print("Gracz 2 wygral")
      g2+=1
  return iteracja

ile=[]
suma=0
wmin=sys.maxint
wmax=0
for i in range(0,1000):
    w=rozgrywka()
    if w < wmin:
        wmin=w
    if w > wmax:
        wmax=w
    ile.append(w)
    suma+=w

print suma*1.0 / len(ile),wmin,wmax,g1,g2
