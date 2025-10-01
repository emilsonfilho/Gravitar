from configs.constants import N
from modules.integration.euler import EulerIntegrator

import numpy as np
class Simulator:
    def __init__(self, integrator, bodies):
        self.integrator = integrator
        self.bodies = bodies
        self.positionHistory = None

    def __computeAllForces(self):
        for body in self.bodies:
            body.force = body.computeTotalForce(self.bodies)
    
    def getSimulationData(self):
        return self.positionHistory

    def run(self):
        self.positionHistory = np.zeros((len(self.bodies), N, 3))

        self.__computeAllForces()

        for step in range(N):
            for i, body in enumerate(self.bodies):
                self.positionHistory[i, step, :] = body.position
            
                self.integrator.step(self.bodies)

                self.__computeAllForces()
        
        return self.getSimulationData()
    