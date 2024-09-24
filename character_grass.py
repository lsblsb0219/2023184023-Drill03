from pico2d import*
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('CIRCLE')

    clear_canvas_now()
    character.draw_now(400,300)
    delay(0.1)
    
    pass    #pass는 빈내용을 뜻함

def run_rectangle():
    print('RECTANGLE')
    pass

while True:
    run_rectangle()
    run_circle()
    break

    
close_canvas()
