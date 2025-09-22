import numpy as np
from configs.constants import G, h

class Body:
    def __init__(self, mass, position, velocity, acceleration):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
    
    def __computeGravitationalForce(self, other):
        displacement = other.position - self.position
        return other.mass * (displacement/(np.linalg.norm(displacement) ** 3))
    
    def computeAcceleration(self, bodies):
        a = np.zeros_like(self.position)
        for other in bodies:
            if other != self:
                a += self.__computeGravitationalForce(other)
        a *= G
        return a
    
    def __eulerStep(self, current, rate, step):
        return current + step * rate

    def computeEulerVelocity(self):
        return self.__eulerStep(self.velocity, self.acceleration, h)
    
    def computeEulerPosition(self):
        return self.__eulerStep(self.position, self.velocity, h)