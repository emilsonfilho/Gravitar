import json
import sys

from utils.paths import ProjectPaths

def loadConfig(configPath="config.json"):
    try:
        with open(ProjectPaths.config() / configPath, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"❌ Error: The file was not found at '{configPath}'")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"❌ Error: The file at '{configPath}' is not a valid JSON file.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        sys.exit(1)