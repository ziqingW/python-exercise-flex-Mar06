from turtle import *

def draw(n):
  degrees = (n - 2) * 180
  degree = 180 - degrees/n
  for i in range(n):
    forward(100)
    right(degree)

if __name__ == "__main__":
  draw(6)