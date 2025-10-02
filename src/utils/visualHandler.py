from configs.visualizationMode import VisualizationMode

import matplotlib.pyplot as plt

class VisualizationModeHandler:
    def __init__(self, mode, anim, outFile, fps):
        self.mode = mode
        self.anim = anim
        self.outFile = outFile
        self.fps = fps

    def run(self):
        if self.mode == VisualizationMode.PLOT.value:
            plt.show()
        elif self.mode == VisualizationMode.VIDEO.value:
            self.anim.save(self.outFile, writer="ffmpeg", fps=self.fps)
        elif self.mode == VisualizationMode.BOTH.value:
            plt.show()
            self.anim.save(self.outFile, writer="ffmpeg", fps=self.fps)