from turtle import *

def polygon(n):
    degrees = (n - 2) * 180
    degree = 180 - degrees/n
    for i in range(n):
        forward(100)
        right(degree)

def star():
    for i in range(5):
        forward(100)
        right(144)

def cir():
    circle(100)