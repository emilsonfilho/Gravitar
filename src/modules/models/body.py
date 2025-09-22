import numpy as np
from configs.constants import G, h

class Body:
    def __init__(self, mass, position, velocity, acceleration, force):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.force = force
    
    def computeGravitationalForce(self, other):
        displacement = other.position - self.position
        return other.mass * (displacement/(np.linalg.norm(displacement) ** 3))
    
    def computeTotalForce(self, bodies):
        total_force = np.zeros_like(self.position)
        for other in bodies:
            if other != self:
                total_force += self.computeGravitationalForce(other)
        total_force *= G * self.mass  # F = m * sum( ... )
        return total_force
    
    def computeAcceleration(self, bodies):
        a = np.zeros_like(self.position)
        for other in bodies:
            if other != self:
                a += self.__computeGravitationalForce(other)
        a *= G
        return a