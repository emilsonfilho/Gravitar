from modules.integration.integrator import Integrator
from modules.physics.forces	 import computeAllAccelerations

class EulerIntegrator(Integrator):
    def step(self, bodies):
        accelerations = computeAllAccelerations(bodies)
        newStates = []
        for body, acc in zip(bodies, accelerations):
            newVel = body.computeEulerVelocity()
            newPos = body.computeEulerPosition()
            newStates.append([newPos, newVel, acc])
        return newStates