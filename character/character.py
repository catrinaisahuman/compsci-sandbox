from pygame.math import Vector2
import pygame
import pgzero.actor
import steeringForces

class Character:
    def __init__(self, image, pos, state, turn=1, speed=7):
        self.pos = Vector2(pos)
        self.heading = Vector2(0,0)
        self.velocity = Vector2(self.heading)
        #self.player = pgzero.actor.Actor(image)
        self.imageName = image
        self.speed = speed
        self.accel = Vector2()

    def update(self):
        #if self.accel != (0,0):
        #    self.velocity = self.velocity + self.accel
        self.velocity = self.velocity*0.9
        self.pos = self.pos + self.velocity
        

    def draw(self, layer):
        #layer.blit(self.imageName, self.pos)
        layer.draw.filled_circle(self.pos, 4, 'black')
#        self.player.draw()
#       self.player.x = self.pos[0]
#        self.player.y = self.pos[1]
#        self.player.angle = -self.angle
#        layer.draw.line(self.pos, self.pos + Vector2.normalize(self.steering)*50, 'black')

        
wind = Vector2()
