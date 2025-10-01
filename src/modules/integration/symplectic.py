from configs.constants import h
from modules.integration.integrator import Integrator

class SymplecticEulerIntegrator(Integrator):
    def step(self, bodies):
        for body in bodies:
            body.velocity += (body.force / body.mass) * h
        
        for body in bodies:
            body.position += body.velocity * h