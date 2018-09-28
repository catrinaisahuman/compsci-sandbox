import character
import steeringForces
import pgzrun
from pygame.math import Vector2
import random
import time


WIDTH = 800
HEIGHT = 600

count = 10000
characters = []

clickPos = (400, 300)
windDist = 100
frame = -1

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
    global clickPos, windDist, frame
    frame += 1
    if frame%15 == 0:
        clickPos = (random.randint(0,800), random.randint(0,600))

    for c in characters:
        c.velocity = steeringForces.wind(c.velocity, c.pos, clickPos, windDist)
        c.color(clickPos, windDist)   
        c.update()


pgzrun.go()
