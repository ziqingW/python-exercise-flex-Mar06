from turtle import *

speed(9)
bond_size = 43
clamp_size = 48
angle = 60

# function to build bond
def bridge(fillColor):
  color(fillColor, fillColor)
# record two positions respectively: one for building clamps,
# one for building other bonds
  global position_clamp
  global position_block
  fill(True)
  position_clamp = pos()
  right(angle)
  forward(bond_size * 2)
  position_block = pos()
  right(angle)
  forward(bond_size)
  right(180 - angle)
  forward(bond_size * 3)
  right(180 - angle)
  forward(bond_size)
  fill(False)

# function to build middle parts
def middle(fillColor1, fillColor2):
# upper half
  color(fillColor1, fillColor1)
  up()
  left(180 - angle)
  forward(5)
  down
  fill(True)
  forward(bond_size - 5)
  right(180 - angle)
  forward(bond_size)
  right(angle)
  forward(bond_size - 5)
  right(180 - angle)
  forward(bond_size)
  fill(False)
# lower half  
  left(180 - angle)
  forward(10)
  left(angle)
  color(fillColor2, fillColor2)
  fill(True)
  forward(bond_size)
  right(angle)
  forward(bond_size - 5)
  right(180 - angle)
  forward(bond_size)
  right(angle)
  forward(bond_size - 5)
  fill(False)

# function to build big clamp parts, the top left one is a model,
# which can be replicated by verizonal reverse (v_reverse = True) or horizonal reverse (h_reverse = True)
def clamp(fill_color, h_reverse = False, v_reverse = False):
  if h_reverse and v_reverse:
    left(180)
    clamp_angle = angle
  elif h_reverse and not v_reverse:
    clamp_angle = 360 - angle
  elif v_reverse and not h_reverse:
    left(180)
    clamp_angle = 360 - angle
  else:
    clamp_angle = angle
  color(fill_color, fill_color)
  fill(True)
  left(180)
  forward(clamp_size * 2)
  left(clamp_angle)
  forward(clamp_size)
  left(180 - clamp_angle)
  forward(clamp_size * 3)
  left(180 - clamp_angle)
  forward(clamp_size)
  fill(False)

# reset function to help cursor heading back to default
def reset(position):
  up()
  home()
  goto(position)
  down()
  
# make background
def bgd(fillColor):
  color(fillColor, fillColor)
  fill(True)
  for i in range(2):
    forward(390)
    right(90)
    forward(200)
    right(90)
  fill(False)
  
# goto the starting point
# draw background first
up()
goto(-195, 180)
down()
bgd("black")
# start drawing!
up()
goto(-68, 160)
down()
bridge("#4ed852")
reset(position_clamp)
clamp("#288c2b")
reset(position_block)
right(angle)
bridge("#274d89")
reset(position_block)
clamp("#719fe8", True, False)
reset(position_clamp)
middle("#719fe8", "#f9d7ca")
up()
forward(5)
right(180 - angle)
forward(bond_size)
right(angle)
forward(2 * bond_size)
down()
right(180 - angle)
bridge("#db3b18")
reset(position_clamp)
clamp("#e07518", True, True)
reset(position_block)
left(180 - angle)
bridge("#b7b4ae")
reset(position_block)
clamp("#f4f4f2", False, True)