from pico2d import*
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('CIRCLE')

    r, cx, cy = 300, 800 // 2, 600 // 2
    # 400을 쓰지 않는 이유는 화면 크기의 반이다는 것을 보여주기 위함
    
    for degree in range(0, 360, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        clear_canvas_now()
        character.draw_now(x,y)
        delay(0.1)
    
    # pass    # pass는 빈내용을 뜻함

def run_top():
    print('TOP')
    pass

def run_right():
    print('RIGHT')
    pass

def run_bottom():
    print('BOTTOM')
    pass

def run_left():
    print('LEFT')
    pass


def run_rectangle():
    print('RECTANGLE')

    run_top()
    run_right()
    run_bottom()
    run_left()
    
    pass

while True:
    # run_circle()
    run_rectangle()
    
    break

    
close_canvas()
