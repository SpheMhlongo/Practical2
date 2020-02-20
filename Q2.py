#!/usr/bin/python3

import turtle

window = turtle.Screen()
tracer = turtle.Turtle()
tracer.pensize(2)

window.bgcolor("black")

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
	move_to(tracer, -200 + 90*i, 0)
	draw(tracer, i+3, colour=["chartreuse", "yellow", "orange", "brown"][i])

turtle.done()