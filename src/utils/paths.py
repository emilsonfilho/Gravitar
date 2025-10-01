from pathlib import Path

class ProjectPaths:
    baseDir = Path(__file__).resolve().parent.parent

    @classmethod
    def config(cls):
        return cls.baseDir / "config"