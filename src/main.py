from modules.models.simulator import Simulator
from modules.integration.crank import CrankNicolsonIntegrator
from modules.render.visualization import visualizePositions
from utils.configLoader import ConfigLoader

import numpy as np
import sys

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