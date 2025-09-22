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
    
    # Trecho de visualization.py (CORRIGIDO)
    def update(frame, records, points):
        for i, point in enumerate(points):
            # Acessando na ordem correta: [corpo, frame, coordenada]
            point.set_data([records[i, frame, 0]], [records[i, frame, 1]])
            point.set_3d_properties([records[i, frame, 2]])
        return points
    
    #anim = FuncAnimation(fig, update, frames=N, interval=50, blit=True)
    # Linha CORRIGIDA
    anim = FuncAnimation(fig, update, frames=N, fargs=(records, points), interval=50, blit=True)
    anim.save(outFile, writer="ffmpeg", fps=animationRate)