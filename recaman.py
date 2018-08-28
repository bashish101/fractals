import turtle
import canvasvg

def setup_window():
	window = turtle.Screen()
	window.setup(width = 1., height = 1.)
	window.bgcolor('black')
	window.title('Recamán sequence visualization')

	width = turtle.window_width()
	height = turtle.window_height()
	return (width, height)

def save_output():
	canvas = turtle.getscreen().getcanvas()
	canvasvg.saveall('recaman.svg', canvas)

def plot_recaman(width, 
		 height, 
		 x_start = None, 
		 y_start = None,
		 x_offset = 30,
		 y_offset = 30,
		 angle = 120, 
		 scale = 4, 
		 n = 200):
	if x_start is None:
		x_start = -int(width / 2) + x_offset
	if y_start is None:
		y_start = int(height / 2) - y_offset

	span = 180
	sequence = [0]	

	turtle.delay(0.1)
	turtle.pen(pensize = int(round(scale/2)), pencolor = 'lightblue')

	turtle.setheading(-angle)

	turtle.up()
	turtle.goto(x_start, y_start)
	turtle.down()
	for idx in range(1, n):
		prev = sequence[idx - 1] - idx
		next = sequence[idx - 1] + idx
		if (prev in sequence) or (prev < 0):
			sequence.append(next)
		else:
			sequence.append(prev)
		
		radius = scale * 0.5 * abs(sequence[idx] - sequence[idx - 1])

		# Go clockwise (if angle is -90 and radius positive, draws forward)
		# if angle is 90 and radius negative, draws backward)
		if sequence[idx] > sequence[idx - 1] and idx % 2 == 0:
			radius *= -1
		elif sequence[idx] < sequence[idx - 1] and idx % 2 != 0:
			radius *= -1

		turtle.circle(radius, span)

	turtle.hideturtle()
	save_output()
	turtle.done()

if __name__ == '__main__':
	x_off = 10
	y_off = 10
	w, h = setup_window()

	x_pos = -int(w / 2) + x_off
	y_pos = 0 

	plot_recaman(w, h, 
		     x_start = x_pos, y_start = y_pos, 
		     x_offset = x_off, y_offset = y_off, 
		     angle = 90, 
		     scale = 5.5,
		     n = 101)

