# File: PanamaFlag.py
# Student:
# UT EID:
# Course Name: CS303E
#
# Date: 12/17/2022
# Description of Program: Practice with turtle graphics

import turtle

turtle.colormode(255)
ttl = turtle.Turtle()


def main():
    ttl.penup()
    ttl.fillcolor(255, 255, 255)
    draw_rectangle(-300, 200)
    ttl.right(90)
    ttl.penup()
    ttl.fillcolor(218, 18, 26)
    draw_rectangle(0, 200)
    ttl.right(90)
    ttl.penup()
    ttl.fillcolor(7, 35, 87)
    draw_rectangle(-300, 0)
    ttl.right(90)
    ttl.penup()
    ttl.fillcolor(255, 255, 255)
    draw_rectangle(0, 0)
    ttl.penup()

    ttl.fillcolor(7, 35, 87)
    draw_star(-150, 100)

    ttl.fillcolor(218, 18, 26)
    draw_star(150, -100)



def draw_rectangle(x, y):
    ttl.goto(x, y)
    ttl.begin_fill()
    ttl.pendown()
    ttl.forward(300)
    ttl.right(90)
    ttl.forward(200)
    ttl.right(90)
    ttl.forward(300)
    ttl.right(90)
    ttl.forward(200)
    ttl.setheading(90)
    ttl.end_fill()
   

def draw_star(x, y):
    ttl.goto(x + 10, y - (0.105572809 * 50))
    ttl.setheading(0)
    
    sideOfStar = 40
    angle = 144
    
    # Fill the colour as of your choice.
    ttl.begin_fill()
    ttl.pendown()
    
    for _ in range(5):
        ttl.forward(sideOfStar)
        ttl.right(angle)
        ttl.forward(sideOfStar)
        ttl.right(72 - angle)
        
    ttl.end_fill()
    ttl.penup()
 
if __name__ == '__main__':
    main()
