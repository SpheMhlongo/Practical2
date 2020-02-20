#!/usr/bin/python3

import turtle

tracer = turtle.Turtle()
tracer.pensize(2)

def draw(t, sides, length=80, colour="black"):
	t.color(colour)

	for i in range(sides):
		t.forward(length)
		t.left((360/sides))

def move_to(t, x, y):
	t.penup()
	t.setpos(x, y)
	t.pendown()

for i in range(4):
	move_to(tracer, -200 + 100*(i*1.5), 0)
	draw(tracer, i+3)

turtle.done()