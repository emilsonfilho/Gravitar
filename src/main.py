from modules.models.body import Body
from modules.models.simulator import Simulator
from modules.integration.crank import CrankNicolsonIntegrator
from modules.render.visualization import visualizePositions
from utils.configLoader import ConfigLoader

import numpy as np
import sys


"""
sun = Body("Sol", 1.9885e30, np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]))
earth = Body("Terra", 5.972e24, np.array([1.495e11, 0.0, 0.0]), np.array([0.0, 29.78e3, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0,0.0,0.0]))
moon = Body("Lua", 7.35e22, np.array([1.496e11, 3.844e8, 0.0]), np.array([1022.0, 29780.0, 0.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0,0.0,0.0]))
"""


# sun = Body(
#     name="Corpo 1",
#     mass=1,
#     position=np.array([0.5773502691896258, 0.0, 0.0]),
#     velocity=np.array([0.0, 0.7598356856515927, 0.0]),
#     acceleration=np.array([0.0, 0.0, 0.0]),
#     force=np.array([0.0, 0.0, 0.0])
# )

# # Um "Planeta" orbitando o Sol
# earth = Body(
#     name="Corpo 2",
#     mass=1,
#     position=np.array([-0.2886751345948128, 0.5, 0.0]), # Posição inicial
#     velocity=np.array([-0.6580370064762464, -0.37991784282579616, 0.0]), # Velocidade para manter a órbita
#     acceleration=np.array([0.0, 0.0, 0.0]),
#     force=np.array([0.0, 0.0, 0.0])
# )

# # Uma "Lua" orbitando o Planeta
# moon = Body(
#     name="Corpo 3",
#     mass=1,
#     position=np.array([-0.2886751345948132, -0.5, 0.0]), # Posição inicial próxima ao planeta
#     velocity=np.array([0.6580370064762461, -0.37991784282579666, 0.0]), # Velocidade do planeta + velocidade orbital
#     acceleration=np.array([0.0, 0.0, 0.0]),
#     force=np.array([0.0, 0.0, 0.0])
# )



if len(sys.argv) < 2:
    print("Error: You must provide a configuration file path as a command-line argument.")
    print("Usage: python3 main.py <path_to_your_config_file>")
    sys.exit(1)

def euler():
    data = ConfigLoader.loadConfig(sys.argv[1])['bodies']
    bodies = ConfigLoader.load(data)

    integrator = CrankNicolsonIntegrator()

    for body in bodies:
        body.force = body.computeTotalForce(bodies)

    positionHistory = Simulator(integrator, bodies).run()
    visualizePositions(np.array(positionHistory))
euler()