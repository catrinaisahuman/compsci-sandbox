import character
import steeringForces
import pgzrun
from pygame.math import Vector2
import random


WIDTH = 800
HEIGHT = 600

count = 10000
characters = []

didClick = False
clickPos = (400, 300)
def draw():
    global clickPos
    screen.fill('white')
    for c in characters:
        c.draw(screen)
    screen.draw.line(characters[0].pos, clickPos, 'black')
    
for i in range(count):
    c = character.Character('waluigi', (random.randint(0,800), random.randint(0,600)), 0)
    characters.append(c)

def update():
    global didClick, clickPos
    
    if didClick == True:
        for c in characters:
            c.velocity = steeringForces.wind(c.velocity, c.pos, clickPos)
        didClick = False    
    for c in characters:
         c.update()
    
def on_mouse_down(pos):
    global didClick, clickPos
    didClick = True
    clickPos = Vector2(pos)

pgzrun.go()
