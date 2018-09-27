from pygame.math import Vector2
import pygame
import math
windSpeed = 200

def wind(velocity, pos, clickPos):
    windForce = Vector2(Vector2(pos - clickPos))
    windVelocity = velocity + (windForce) * min((windSpeed/pos.distance_squared_to(clickPos)), windSpeed)
    return windVelocity

def seek(velocity, pos, clickPos):
    targetDir = Vector2(clickPos - pos)
    steeringForce = (targetDir - velocity).normalize()
    seekVelocity = velocity + steeringForce
    return seekVelocity
