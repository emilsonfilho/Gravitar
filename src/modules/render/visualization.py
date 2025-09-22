from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

from configs.constants import N

import matplotlib.pyplot as plt

def visualizePositions(records, bodyNames, outFile="sim.mp4", animationRate=20):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    
    allX = records[:,:,0].flatten()
    allY = records[:,:,1].flatten()
    allZ = records[:,:,2].flatten()
    ax.set_xlim(allX.min()*0.9, allX.max()*1.1)
    ax.set_ylim(allY.min()*0.9, allY.max()*1.1)
    ax.set_zlim(allZ.min()*0.9, allZ.max()*1.1)
    ax.set_aspect("equal")
    
    colors = ["yo","bo","ko"]
    points = [ax.plot([], [], c, label=name)[0] for c, name in zip(colors, bodyNames)]
    
    ax.legend()
    
    def update(frame):
        for i, point in enumerate(points):
            point.set_data([records[frame, i, 0]], [records[frame, i, 1]])
            point.set_3d_properties([records[frame, i, 2]])
        return points
    
    anim = FuncAnimation(fig, update, frames=N, interval=50, blit=True)
    anim.save(outFile, writer="ffmpeg", fps=animationRate)