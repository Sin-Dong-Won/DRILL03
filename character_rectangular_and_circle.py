from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

Wid = 800
Hei = 600

Pi = (float)(math.radians(1))

def rectangular_move():
    x = 0
    y = 90

    while(x < 800):
        clear_canvas_now()
        #grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 5
        delay(0.01)

    while(y < 600):
        clear_canvas_now()
       # grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 5
        delay(0.01)


    while(x > 0):
        clear_canvas_now()
        #grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 5
        delay(0.01)

    while(y > 90):
        clear_canvas_now()
        #grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 5
        delay(0.01)  

def circle_move():

    for i in range(0, 360):
        clear_canvas_now()
        #grass.draw_now(400, 30)
        character.draw_now(math.sin(Pi * (180 - i)) * Wid / 2 + Wid / 2, math.cos(Pi * (180 - i)) * Hei / 2 + Hei / 2 + 90)
        delay(0.01) 


while(True):
    circle_move()
        

        
    

    
