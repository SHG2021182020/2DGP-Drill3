from pico2d import *

def run_rectangle():
	print('RECTANGLE');
	pass

def run_circle():
	print('CIRCLE')
	pass

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')
i = 0
for i in range(10):
    run_rectangle()
    run_circle()

close_canvas()