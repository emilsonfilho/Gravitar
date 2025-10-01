import json
import sys
import numpy as np

from modules.models.body import Body
from utils.paths import ProjectPaths

class ConfigLoader:
    @staticmethod
    def loadConfig(configPath="config.json"):
        try:
            with open(ProjectPaths.config() / configPath, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"❌ Error: The file was not found at '{ProjectPaths.config() / configPath}'. Please check the path and try again.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"❌ Error: The file at '{configPath}' is not a valid JSON file.")
            sys.exit(1)
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            sys.exit(1)

    @staticmethod
    def load(data):
        return [
            Body(
                mass=b['mass'],
                position=np.array(b['position']),
                velocity=np.array(b['velocity']),
            ) for b in data
        ]
