import turtle
# turtle.setup(500,300)      # Set a canvas 500 wide and 300 high, located in the center of the screen
# turtle.penup()                 #Lift the brush, do not draw, adjust the position first
# turtle.pensize(2)             #Set the brush width to 2
# turtle.goto(0,50)             # Move the brush to (0,50).
# turtle.setheading(180)     # Turn the brush direction to true west
# turtle.pendown()             # Prepare to draw graphics
# turtle.circle(50,180)        # Draw an arc with a radius of 50 and an angle of 180
# turtle.exitonclick()               # Do not close the canvas when drawing is complete



# turtle.setup(800,500)           # Set a canvas 500 wide and 300 high, located in the center of the screen
# turtle.begin_fill()                  # Ready to start populating graphics
# turtle.color("gold","gold")   # Set the color of the brush and fill to be gold
# turtle.penup()
# turtle.goto(0,50)             # Move the brush to (0,50).
# turtle.circle(100,-180)                    # Draw a circle with a radius of 50
# turtle.end_fill()                     # Filling is complete
# turtle.penup()                 #Lift the brush, do not draw, adjust the position first
# turtle.hideturtle()                # Hides brush shapes
# turtle.exitonclick()               # Do not close the canvas when drawing is complete

import turtle

# Create a Turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(2)

# Draw the heart shape
t.begin_fill()
t.fillcolor("red")
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
