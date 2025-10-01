from modules.models.simulator import Simulator
from modules.integration.symplectic import SymplecticEulerIntegrator
from modules.render.visualization import visualizePositions
from utils.configLoader import ConfigLoader

import numpy as np
import sys

if len(sys.argv) < 3:
    print("Error: You must provide a configuration file path and a visualization mode as command-line arguments.")
    print("Usage: python3 main.py <path_to_your_config_file> <visualization_mode>")
    sys.exit(1)

def runSimulation():
    data = ConfigLoader.loadConfig(sys.argv[1])['bodies']
    bodies = ConfigLoader.load(data)

    integrator = SymplecticEulerIntegrator()

    for body in bodies:
        body.force = body.computeTotalForce(bodies)

    positionHistory = Simulator(integrator, bodies).run()
    visualizePositions(np.array(positionHistory), mode=sys.argv[2])
runSimulation()