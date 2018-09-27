from pygame.math import Vector2
import pygame
import pgzero.actor
import steeringForces

class Character:
    def __init__(self, image, pos, state, turn=1, speed=7):
        self.pos = Vector2(pos)
        self.heading = Vector2(0,0)
        self.velocity = Vector2(self.heading)
        self.imageName = image
        self.speed = speed
        self.accel = Vector2()

    def update(self):
        self.velocity = self.velocity*0.9
        self.pos = self.pos + self.velocity
        

    def draw(self, layer):
        layer.draw.filled_circle(self.pos, 4, 'black')
        
