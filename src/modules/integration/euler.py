from modules.integration.integrator import Integrator
from modules.physics.forces	 import computeAllAccelerations
from configs.constants import h

class EulerIntegrator(Integrator):
    def step(self, bodies):
        accelerations = computeAllAccelerations(bodies)
        newStates = []
        for body, acc in zip(bodies, accelerations):
            newVel = body.velocity + h * acc
            newPos = body.position + h * body.velocity
            newStates.append([newPos, newVel, acc])
        return newStates