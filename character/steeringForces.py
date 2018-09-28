from pygame.math import Vector2
import pygame
import math
windSpeed = 200

def wind(velocity, pos, clickPos, windDist):
    windForce = Vector2(Vector2(pos - clickPos))
    if pos.distance_to(clickPos) > windDist or pos.distance_to(clickPos) == 0:
    	windForce =Vector2(0, 0)
    	windVelocity = Vector2(0,0)
    else:
    	windVelocity = velocity + (windForce) * min((windSpeed/pos.distance_squared_to(clickPos)), windSpeed)
    return windVelocity

def seek(velocity, pos, clickPos):
    targetDir = Vector2(clickPos - pos)
    steeringForce = (targetDir - velocity).normalize()
    seekVelocity = velocity + steeringForce
    return seekVelocity
