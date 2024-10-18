from turtle import *

#we want to paint a house


speed(30)
#step 1: draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)



#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
        


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)          
end_fill()


color("purple")
left(30)
forward(70)
left(90)
color("blue")
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

color("purple")
left(90)
forward(90)
left(90)
forward(200)
left(90)
forward(90)
left(90)
color("blue")
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()
right(90)
color("purple")
forward(130)
right(90)
forward(70)
right(90)
color("yellow")
begin_fill()
forward(120)
left(90)
forward(60)
left(90)
forward(120)
end_fill()








exitonclick()    