import turtle 
import os

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Raquette A
raquette_a = turtle.Turtle()
raquette_a.speed(0)
raquette_a.shape("square")
raquette_a.color("white")
raquette_a.shapesize(stretch_wid=5, stretch_len=1)
raquette_a.penup()
raquette_a.goto(-350, 0  )



 # Raquette B 
raquette_a = turtle.Turtle()
raquette_a.speed(0)
raquette_a.shape("square")
raquette_a.color("white")
raquette_a.shapesize(stretch_wid=5, stretch_len=1)
raquette_a.penup()
raquette_a.goto(350, 0  )

# Balle 
balle = turtle.Turtle()
balle.speed(0)
balle.shape("square")
balle.color("white") 
balle.penup()
balle.goto(0, 0  )
balle.dx = 2
balle.dy = -2   

# Pen 
pen = turtle.Turtle
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

#Function
def raquette_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def raquette_a_down():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def raquette_b_down():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def raquette_b_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

#Keyboard bind
wn.listen()
wn.onkeypress(raquette_a_up, "a")
wn.onkeypress(raquette_a_down, "d")
wn.onkeypress(raquette_b_up, "Up")
wn.onkeypress(raquette_b_down, "Down")

# Main game loop
while True : 
	wn.update()

#bouger la balle 
ball.sextx(balle.xcor() + ball.dx)
ball.sety(balle.ycor() + ball.dy)


# Border checking 
if balle.ycor() > 290:
	balle.stey(290)
	balle.dy *= -1

if balle.ycor() < -290:
	balle.stey(-290)
	balle.dy *= -1

if balle.xcor() > 390:
	balle.goto(0, 0)
	balle.dx *= -1

if balle.xcor() < -390:
	balle.goto(0, 0)
	balle.dx *= -1