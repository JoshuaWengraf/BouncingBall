# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:28:00 2021

Bouncing ball animation. 

@author: jweng
"""

import turtle
import time
from PIL import Image


def save(counter = [1]):
    turtle.getcanvas().postscript(file = "BouncingBall{0:03d}.eps".format(counter[0])) 
    turtle_img = Image.open("BouncingBall{0:03d}.eps".format(counter[0]))
    turtle_img.save("BouncingBall{0:03d}.png".format(counter[0]), "png")
    
    counter[0] += 1
    print(counter)
    turtle.ontimer(save, int(1000/FRAMES_PER_SECOND))
    

FRAMES_PER_SECOND = 30


window = turtle.Screen()
window.bgcolor("white")
window.title("Bouncing Ball")

ball = turtle.Turtle()
ball.shape("circle")

ball.penup() # no drawn line
ball.speed(0) # set initial speed

y = 150 # initial position
v = -4 # initial speed
g = -0.15 # gravitational constant

timelimit = 60

t = 0

save()

start_time = time.time()

running = True
while True:
    v = v + g*t
    y = y + g*t**2 + v*t
    
    ball.sety(y)
        
    if y < -100:
        v *= -1
    
    elapsed_time = time.time() - start_time
    
    if elapsed_time >= timelimit:
        print('animation finished')
        break
    
    t = t + 0.01

turtle.clearscreen()
turtle.bye()


        
