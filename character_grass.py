from pico2d import*
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_character(x, y):
    clear_canvas_now()
    character.draw_now(x,y)
    delay(0.1)

def run_circle():
    print('CIRCLE')

    r, cx, cy = 300, 800 // 2, 600 // 2
    # 400을 쓰지 않는 이유는 화면 크기의 반이다는 것을 보여주기 위함
    
    for degree in range(0, 360, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        
        draw_character(x,y)
    
    #pass    # pass는 빈내용을 뜻함

def run_top():
    print('TOP')
    for x in range(0, 800, 10):
        draw_character(x, 550)

def run_right():
    print('RIGHT')
    for y in range(550, 0, -10):
        draw_character(790, y)

def run_bottom():
    print('BOTTOM')
    for x in range(800, 0, -10):
        draw_character(x, 0)

def run_left():
    print('LEFT')
    for y in range(0, 550, 10):
        draw_character(0, y)


def run_rectangle():
    print('RECTANGLE')

    #run_top()
    #run_right()
    #run_bottom()
    run_left()


while True:
    #run_circle()
    run_rectangle()
    
    break

    
close_canvas()
