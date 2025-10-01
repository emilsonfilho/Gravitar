import numpy as np
from configs.constants import G, h

class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.zeros(3, dtype=float)
        self.force = np.zeros(3, dtype=float)
    
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