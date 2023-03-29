import turtle
#create a turtle object
heart=turtle
#set the turtle's speed
heart.speed(10)
#move the turtle to the starting point
heart.penup()
heart.goto(0,-150)
heart.pendown()
#draw the upper part of the heart
heart.begin_fill()
heart.color("black","red")
heart.left(45)
heart.forward(200)
heart.circle(100,180)
heart.right(90)
heart.circle(100,180)
heart.forward(200)
heart.end_fill()

#draw the lower part of the heart
heart.penup()
heart.goto(0,-250)
heart.pendown()
heart.begin_fill()
heart.circle(100)
heart.end_fill()
heart.hideturtle()
turtle.done()



