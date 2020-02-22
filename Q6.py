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

	x_axis_labels = turtle.Turtle()
	y_axis_labels = turtle.Turtle()

	x_axis_labels.penup()
	x_axis_labels.forward(5)
	x_axis_labels.left(90)
	x_axis_labels.forward(amplitude)
	x_axis_labels.left(180)

	x_label_value = 1

	for i in range(5):
		if i != 2:
			x_axis_labels.write(x_label_value - 0.5*i)
		x_axis_labels.forward(amplitude / 2)
	x_axis_labels.ht()

	y_axis_labels.penup()
	y_axis_labels.forward(degress_start)
	y_axis_labels.left(90)
	y_axis_labels.forward(5)
	y_axis_labels.right(90)

	y_label_value = 1

	for i in range(5):
		if i != 2:
			y_axis_labels.write(int(degress_start + ((degress_end-degress_start) / 4)*i))
		y_axis_labels.forward((degress_end-degress_start) / 4)
	y_axis_labels.ht()

	for x in range(degress_start, degress_end+1):
		y = math.sin(x * (math.pi/180)) * amplitude
		
		t1.goto(x, y)

draw_sin_graph(tracer1, tracer2)

turtle.done()