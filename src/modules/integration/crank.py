from configs.constants import h
from modules.integration.integrator import Integrator

class CrankNicolsonIntegrator(Integrator):
    def step(self, bodies):
        #newStates = []
        for body in bodies:
            body.velocity += (body.force / body.mass) * h
        
        for body in bodies:
            body.position += body.velocity * h
        '''
        for body in bodies:
            newPos = body.position + body.velocity * h + body.force/body.mass * (h**2)
            newVel = (newPos - body.position) / h
            newForce = body.mass * (newVel - body.velocity) / h
            newStates.append([newPos, newVel, newForce])
        return newStates
        '''