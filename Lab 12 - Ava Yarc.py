
#import code from lab. Line 4 - 22

import turtle

class Point(object):
    
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
        
    def draw_action(self):
        turtle.dot()

#creates a box
class Box(Point):

    def __init__(self,x1,y1,width,height,color):
        super().__init__(x1,y1,color) #use inputs from class Point
        self.width = width
        self.height = height

    #draw the box
    def draw_action(self): #draws box
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.penup()

#color box
class BoxFilled(Box):

    def __init__(self,x1,y1,width,height,color,fillcolor):
        super().__init__(x1,y1,width,height,color) #use inputs from class Box
        self.fillcolor = fillcolor

    def draw_action(self): #draws box and colors it in
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self) #calling draw action from class Box to make code more simple
        turtle.end_fill()

#creating a circle       
class Circle(Point):

    def __init__(self,x1,y1,radius,color):
        super().__init__(x1,y1,color) #use inputs from class Point
        self.radius = radius

    def draw_action(self): #draw circle
        turtle.circle(self.radius)

#color circle
class CircleFilled(Circle):

    def __init__(self,x1,y1,radius,color,fillcolor):
        super().__init__(x1,y1,radius,color) #use inputs from class Circle
        self.fillcolor = fillcolor

    def draw_action(self): #draws box and colors it in
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self) #calling draw action from class Circle
        turtle.end_fill()
        

