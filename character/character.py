from pygame.math import Vector2
from pygame.math import Vector3
import pygame
import pgzero.actor
import steeringForces
import colorsys

class Character:
    def __init__(self, image, pos, state, turn=1, speed=7):
        self.pos = Vector2(pos)
        self.heading = Vector2(0,0)
        self.velocity = Vector2(self.heading)
        self.imageName = image
        self.speed = speed
        self.accel = Vector2()
        self.circleColor = (0, 0, 0)
        self.maxDist = 1000
        self.baseColor = Vector3(0, 1, 1)
        self.maxColor = Vector3(0, 0, 0)

    def update(self):
        self.velocity = self.velocity*0.9
        self.pos = self.pos + self.velocity
    
    def color(self, clickPos):
        distance = self.pos.distance_to(clickPos)
        print(distance)
        hsvColor = self.baseColor.lerp(self.maxColor, min(distance/self.maxDist, 1))
        hsvColor = colorsys.hsv_to_rgb(hsvColor[0], hsvColor[1], hsvColor[2])
        self.circleColor = (hsvColor[0]*255, hsvColor[1]*255, hsvColor[2]*255)


    def draw(self, layer):
        layer.draw.filled_circle(self.pos, 4, self.circleColor)

