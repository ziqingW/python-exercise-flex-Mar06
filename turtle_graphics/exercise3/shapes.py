from turtle import *

def polygon(n, size, fil, cpen, cfill=None):
  if cfill: 
    color(cpen, cfill)
  else:
    pencolor(cpen)
  degrees = (n - 2) * 180
  degree = 180 - degrees/n
  if fil:
    fill(True)
    for i in range(n):
      forward(size)
      right(degree)
    fill(False)
  else:
    for i in range(n):
      forward(size)
      right(degree)

def star(size, fil, cpen, cfill=None):
  if cfill: 
    color(cpen, cfill)
  else:
    pencolor(cpen)
  if fil:
    fill(True)
    for i in range(5):
      forward(size)
      right(144)
    fill(False)
  else:
    for i in range(5):
      forward(size)
      right(144)

def cir(size, fil, cpen, cfill=None):
  if cfill: 
    color(cpen, cfill)
  else:
    pencolor(cpen)
  if fil:
    fill(True)
    circle(size)
    fill(False)
  else:
    circle(size)