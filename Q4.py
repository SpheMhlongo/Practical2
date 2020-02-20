#!/usr/bin/python3

import turtle
import math

tracer1 = turtle.Turtle()
tracer2 = turtle.Turtle()

def draw_sin_graph(t1, t2, amplitude=100, degress_start=-180, degress_end=180):
	# setup plane
	t1.forward(degress_start)
	t1.forward(2 * degress_end)

	t2.left(90)
	t2.forward(-amplitude)
	t2.forward(2 * amplitude)
	# end setting up plane

	for x in range(degress_start, degress_end+1):
		y = math.sin(x * (math.pi/180)) * amplitude
		
		t1.goto(x, y)


draw_sin_graph(tracer1, tracer2)

turtle.done()