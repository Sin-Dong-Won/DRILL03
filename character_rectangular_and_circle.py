from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

Wid = 800
Hei = 600

Pi = (float)(math.radians(1))

def render_screen(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)    

def rectangular_move():
    print('RECTANGLE')

    # bottom line
    for x in range(50, 750 + 1, 10):
        render_screen(x, 90)
        
    # right line
    for y in range(90, 550 + 1, 10):
        render_screen(750, y)
            
    # top line    
    for x in range(750, 50 - 1, -10):
        render_screen(x, 550)
        
    # left line
    for y in range(550, 90 - 1, -10):
        render_screen(50, y)    

def circle_move():
    print('CIRCLE')
    
    cx, cy, r = 400,300,200    
    for deg in range(-90, 270 + 1, 5):
        x =  cx + r * math.cos(deg / 360 * 2 * math.pi)
        y =  cy + r * math.sin(deg / 360 * 2 * math.pi)
        render_screen(x, y)


while(True):
    rectangular_move()
    circle_move()
    break

close_canvas()

        
    

    
