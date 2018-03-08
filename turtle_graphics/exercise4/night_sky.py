from turtle import *
import random

# bgcolor is not working, use a function to brush a background
def bgd():
  speed(10)
  up()
  goto(-200,200)
  down()
  color((227,232,229), (27, 27, 28))
  fill(True)
  for i in range(4):
    forward(400)
    right(90)
  fill(False)

# make a star generator with random color, size, tilt angle and position  
def star(num):
  for i in range(num):
    color_list = ["pink", "yellow", "blue", "red", "green", "white", "purple", "orange", "cyan"]
    pickColor = color_list[random.randint(0, len(color_list) - 1)] 
    size_list = list(range(10, 61))
    pickSize = size_list[random.randint(0, len(size_list) - 1)]
    angle = random.randint(0, 180)
    position = (random.randint(-180, 180), random.randint(-180, 180))
# let's draw! 
    up()
    goto(position)
    down()
    color(pickColor, pickColor)
    fill(True)
    right(angle)
    for i in range(5):
      forward(pickSize)
      right(144)
    fill(False)
    
if __name__ == "__main__":
  bgd()
  star(77)