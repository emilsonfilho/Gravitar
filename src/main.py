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