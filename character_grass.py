from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.001)

def run_top():
	for x in range(0,800,10):
		draw_boy(x, 0)
	pass

def run_right():
	for y in range(0,600,10):
		draw_boy(800, y)
	pass

def run_bottom():
	for dx in range(0,800,10):
		d = 800 - dx
		draw_boy(d, 600)
	pass

def run_left():
	for dx in range(0,600,10):
		d = 600 - dx
		draw_boy(0, d)
	pass

def run_tri_fir():
	x = 800 // 2 - 50
	y = 600 // 2

	for d in range(0,100):
		draw_boy(x + d, y)
	pass

def run_tri_sec():
	x = 800 // 2 + 50
	y = 600 // 2
	
	for d in range(0,100):
		draw_boy(x - d / 2, y + d)
	pass

def run_tri_thr():
	x = 800 // 2
	y = 600 // 2 + 100
	
	for d in range(0,100):
		draw_boy(x - d / 2, y - d)
	pass

def run_rectangle():
	print('RECTANGLE');

	run_top()
	run_right()
	run_bottom()
	run_left()

	pass

def run_circle():
	print('CIRCLE')

	r = 100
	cx = 800 // 2
	cy = 600 // 2

	for d in range(0, 360):
		x = r * math.cos(math.radians(d)) + cx
		y = r * math.sin(math.radians(d)) + cy
		draw_boy(x, y)

	pass

def run_tri():
	print('triangle')

	run_tri_fir()
	run_tri_sec()
	run_tri_thr()

	pass

while True:
    run_rectangle()
    run_circle()
    run_tri()

close_canvas()