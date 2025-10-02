from modules.models.simulator import Simulator
from modules.integration.symplectic import SymplecticEulerIntegrator
from modules.render.visualization import visualizePositions
from utils.configLoader import ConfigLoader

import numpy as np
import sys

if len(sys.argv) < 3:
    print("Error: Error: You must provide a configuration file and a visualization mode.")
    print("Usage: python3 main.py <config_file> <plot|video|both> [output_file]")
    sys.exit(1)

configFile = sys.argv[1]
mode = sys.argv[2]
outFile = "sim.mp4"

if mode in ["video", "both"]:
    if len(sys.argv) < 4:
        print(f"Error: The '{mode}' mode requires an output filename.")
        print(f"Usage: python3 main.py {configFile} {mode} <output_file>")
        sys.exit(1)
    outFile = sys.argv[3]

def runSimulation():
    data = ConfigLoader.loadConfig(configFile)['bodies']
    bodies = ConfigLoader.load(data)

    integrator = SymplecticEulerIntegrator()

    for body in bodies:
        body.force = body.computeTotalForce(bodies)

    positionHistory = Simulator(integrator, bodies).run()
    visualizePositions(np.array(positionHistory), mode=mode, outFile=outFile)
runSimulation()