#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 22:55:17 2021

@author: bekahsmith
"""

import turtle
import random
import math

turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

class setup():
    def __init__(self):
        self.panel = turtle.Screen()
        self.panel.setup(width=2560, height=1600)
        self.panel.listen()
        
        self.panelz()
        
    def panelz(self):
        self.panel.bgcolor(random.randint(220, 250), random.randint(220, 250), random.randint(220, 250))

        self.how()
        
    def how(self):
        self.how = turtle.Turtle(visible=False)
        self.how.up()
        self.how.goto(-300, -700)
        self.how.color("black")
        self.how.down()
        self.rules = "click the screen to make art. press b, o, p, y, g, or r to change colors."
        self.how.write(self.rules, font=("arial", 12, "normal"))
        self.panel.update()
        
        self.play()
        
    def play(self):
        self.blues = [(158, 195, 209), (130, 179, 196), (102, 163, 183), (78, 144, 166), (78, 144, 166), (58, 146, 166), (58, 146, 166), (37, 93, 106), (27, 67, 75)] 
        self.purps = [(49, 13, 32), (81, 21, 53), (114, 29, 74), (51, 31, 40), (76, 47, 60), (101, 62, 80), (126, 78, 100), (152, 93, 119), (170, 116, 139), (185, 141, 160)] 
        self.greens = [(134, 172, 145), (109, 156, 123), (91, 134, 104), (74, 109, 85), (58, 85, 66), (197, 210, 177), (178, 195, 151), (159, 181, 125), (139, 166, 100), (117, 142, 82)]
        self.yellows = [(221, 227, 140), (212, 219, 107), (202, 211, 74), (247, 248, 180), (243, 245, 143), (240, 242, 105), (236, 239, 67), (232, 235, 30), (203, 206, 18), (166, 169, 15)]
        self.oranges = [(245, 211, 143), (242, 196, 105), (239, 182, 67), (235, 167, 30), (206, 144, 18), (246, 182, 141), (243, 157, 104), (240, 133, 66), (237, 108, 29), (208, 90, 17)]
        self.reds = [(206, 126, 100), (196, 101, 69), (171, 83, 54), (140, 68, 44), (109, 53, 34), (97, 42, 39), (131, 56, 52), (160, 69, 64), (185, 85, 80), (197, 114, 109)]

        self.palette = self.blues
        
        self.pretty = turtle.Turtle(visible=False)
       
        self.panel.onclick(self.prettiest)
        self.panel.onkey(self.bluechange, "b")
        self.panel.onkey(self.orangechange, "o")
        self.panel.onkey(self.purpchange, "p")
        self.panel.onkey(self.greenchange, "g")
        self.panel.onkey(self.yellowchange, "y")
        self.panel.onkey(self.redchange, "r")
        
    def bluechange(self):
        self.palette = self.blues
    
    def purpchange(self):
        self.palette = self.purps
        
    def greenchange(self):
        self.palette = self.greens
        
    def yellowchange(self):
        self.palette = self.yellows
        
    def orangechange(self):
        self.palette = self.oranges
        
    def redchange(self):
        self.palette = self.reds

    def prettiest(self, x, y):
        
        self.x = x
        self.y = y
        self.pretty.up()
        self.pretty.color(random.choice(self.palette))
        self.pretty.goto(x, y)
        self.pretty.down()
        
        #the following code for funky spiral is borrowed from Dr. Z
        self.a = random.randint(23,26)
        self.b = random.randint(22,27) 
        
        self.scale = (random.randint(5,20))
        self.ANGLES = range(0,random.randint(100,460)) # change this depending on your pattern!
        
        for angle in self.ANGLES:
            self.angle = math.radians(angle) # overwrites input to radians (required!)
        
            self.X = self.angle - 1.6*math.cos(self.a*self.angle)
            self.Y = self.angle - 1.6*math.cos(self.b*self.angle)
            self.X*=self.scale # make the image larger so it's visible
            self.Y*=self.scale
            
            self.pretty.goto(self.x+self.X, self.y+self.Y)
            self.panel.update()
        #End borrowed code - thanks Dr. Z!    
        
        self.pretty.forward(random.randint(30,159))
        self.distance = random.randint(15,50)
        self.twist = random.randint(0,359)
        for i in range(random.randint(6,19)):
            self.pretty.forward(self.distance)
            self.pretty.right(self.twist)
        
        self.pretty.forward(random.randint(20,120))
        self.pretty.circle(random.randint(20,200), random.randint(20,350))
        self.pretty.right(random.randint(0,340))
        self.pretty.forward(random.randint(2,80))
        self.pretty.begin_fill()
        self.pretty.circle(random.randint(10,60), random.randint(20,360))
        self.pretty.end_fill()
        
        self.pretty.up()
        self.panel.update()
        
if __name__=='__main__':
    setup()
   
turtle.mainloop()