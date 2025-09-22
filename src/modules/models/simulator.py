from configs.constants import N
from modules.integration.euler import EulerIntegrator

import numpy as np
class Simulator:
    def __init__(self, integrator):
        self.integrator = integrator
    
    def run(self, bodies):
        numBodies = len(bodies)
        dim = len(bodies[0].position)
        
        recordPositions = np.zeros((N, numBodies, dim))
        
        for i in range(N):
            for j, body in enumerate(bodies):
                recordPositions[i, j, :] = body.position
                
            newStates = self.integrator.step(bodies)
            for body, (newPos, newVel, acc) in zip(bodies, newStates):
                body.position = newPos
                body.velocity = newVel
                body.acceleration = acc
            
        return recordPositions
    