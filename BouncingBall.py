# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:28:00 2021

@author: jweng
"""

import turtle
import time
from PIL import Image

def save(counter=[1]):
    turtle.getcanvas().postscript(file = "BouncingBall{0:03d}.eps".format(counter[0]))
    counter[0] += 1
    
    print(counter)
    
    turtle.ontimer(save, int(1000/30))

window = turtle.Screen()
window.bgcolor("white")
window.title("Bouncing Ball")

ball = turtle.Turtle()
ball.shape("circle")

ball.penup()
ball.speed(0)

ball.goto(0, 150)

ball.dy = -2

FRAMES_PER_SECOND = 15

gravity = 0.15

timelimit = 5.3
start_time = time.time()

t = 0


def draw():
    
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)
        
    if ball.ycor() < -100:
        ball.dy *= -1
        
save()

running = True
while True:
    draw()
    
    elapsed_time = time.time() - start_time
    if elapsed_time >= 6:
        print('animation finished')
        break

turtle.bye()

for ctr in range(1, 10):
    turtle_img = Image.open("iceland00" + str(ctr) + ".eps")
    turtle_img.save("iceland00" + str(ctr) + ".png", "png")

for ctr in range(10, 100):
    turtle_img = Image.open("iceland0" + str(ctr) + ".eps")
    turtle_img.save("iceland0" + str(ctr) + ".png", "png")
    

        
