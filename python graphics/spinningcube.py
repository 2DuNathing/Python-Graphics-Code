from math import sin, cos
import turtle
VERTEXES = [(-1, -1, -1), ( 1, -1, -1), ( 1,  1, -1), (-1,  1, -1),
            (-1, -1,  1), ( 1, -1,  1), ( 1,  1,  1), (-1,  1,  1)]
TRIANGLES = [
    (0, 1, 2), (2, 3, 0),
    (0, 4, 5), (5, 1, 0),
    (0, 4, 3), (4, 7, 3),
    (5, 4, 7), (7, 6, 5),
    (7, 6, 3), (6, 2, 3),
    (5, 1, 2), (2, 6, 5)
]
FOV = 400
# Create turtle,
pointer = turtle.Turtle()
# Turn off move time, makes drawing instant,
turtle.tracer(0, 0)
pointer.up()
def rotate(x, y, r):
  s, c = sin(r), cos(r)
  return x * c - y * s, x * s + y * c
counter = 0
while True:
	# Clear screen,
	pointer.clear()
	# Draw,
	for triangle in TRIANGLES:
		points = []
		for vertex in triangle:
			# Get the X, Y, Z coords out of the vertex iterator,
			x, y, z = VERTEXES[vertex]
			# Rotate,
			x, z = rotate(x, z, counter)
			y, z = rotate(y, z, counter)
			x, y = rotate(x, y, counter)
			# Perspective formula,
			z += 5
			f = FOV / z
			sx, sy = x * f, y * f
			# Add point,
			points.append((sx, sy))
		
		# Draw triangle,
		pointer.goto(points[0][0], points[0][1])
		pointer.down()
		pointer.goto(points[1][0], points[1][1])
		pointer.goto(points[2][0], points[2][1])
		pointer.goto(points[0][0], points[0][1])
		pointer.up()
	# Update,
	turtle.update()
	counter += 0.025