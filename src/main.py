from configs.constants import N,h
from modules.models.body import Body
from modules.models.simulator import Simulator
from modules.integration.euler import EulerIntegrator
from modules.integration.crank import CrankNicolsonIntegrator
from modules.render.visualization import visualizePositions

import numpy as np

"""
sun = Body("Sol", 1.9885e30, np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]))
earth = Body("Terra", 5.972e24, np.array([1.495e11, 0.0, 0.0]), np.array([0.0, 29.78e3, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0,0.0,0.0]))
moon = Body("Lua", 7.35e22, np.array([1.496e11, 3.844e8, 0.0]), np.array([1022.0, 29780.0, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0,0.0,0.0]))
"""

a = 0.97000436
b = 0.24308753


sun = Body(
    name="Corpo 1",
    mass=1,
    position=np.array([0.347111, 0.532728, 0.0]),
    velocity=np.array([0.839031, -0.743108, 0.25]),
    acceleration=np.array([0.0, 0.0, 0.0]),
    force=np.array([0.0, 0.0, 0.0])
)

# Um "Planeta" orbitando o Sol
earth = Body(
    name="Corpo 2",
    mass=1,
    position=np.array([-0.34711, -0.532728, 0.0]), # Posição inicial
    velocity=np.array([0.839031, -0.743108, 0.25]), # Velocidade para manter a órbita
    acceleration=np.array([0.0, 0.0, 0.0]),
    force=np.array([0.0, 0.0, 0.0])
)

# Uma "Lua" orbitando o Planeta
moon = Body(
    name="Corpo ",
    mass=1,
    position=np.array([0.0, 0.0, 0.0]), # Posição inicial próxima ao planeta
    velocity=np.array([-1.678062e-1, 1.486216, -0.5]), # Velocidade do planeta + velocidade orbital
    acceleration=np.array([0.0, 0.0, 0.0]),
    force=np.array([0.0, 0.0, 0.0])
)


def euler():
    bodies = [sun, earth, moon]
    integrator = CrankNicolsonIntegrator()

    for body in bodies:
        body.force = body.computeTotalForce(bodies)

    positionHistory, bodyNames = Simulator(integrator, bodies).run()
    visualizePositions(np.array(positionHistory), bodyNames)
euler()