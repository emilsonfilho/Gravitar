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


sun = Body(
    name="Sol",
    mass=1000.0,
    position=np.array([0.0, 0.0, 0.0]),
    velocity=np.array([0.0, 0.0, 0.0]),
    acceleration=np.array([0.0, 0.0, 0.0]),
    force=np.array([0.0, 0.0, 0.0])
)

# Um "Planeta" orbitando o Sol
earth = Body(
    name="Planeta",
    mass=10.0,
    position=np.array([100.0, 0.0, 0.0]),
    velocity=np.array([0.0, 2.583e-5, 0.0]), # Velocidade para manter a órbita
    acceleration=np.array([0.0, 0.0, 0.0]),
    force=np.array([0.0, 0.0, 0.0])
)

# Uma "Lua" orbitando o Planeta
moon = Body(
    name="Lua",
    mass=10.0,
    position=np.array([45.0, 100.0, 0.0]), # Posição inicial próxima ao planeta
    velocity=np.array([0.0, 3e-5, 0.0]), # Velocidade do planeta + velocidade orbital
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