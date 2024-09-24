from pico2d import*
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('CIRCLE')
    pass    #pass는 빈내용을 뜻함

def run_rectangle():
    print('RECTANGLE')
    pass

while True:
    run_rectangle()
    run_circle()

    
close_canvas()
