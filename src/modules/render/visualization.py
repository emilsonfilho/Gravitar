from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

from configs.constants import N

import matplotlib.pyplot as plt

def visualizePositions(records, bodyNames, outFile="sim.mp4", animationRate=20):
    fig = plt.figure(facecolor="black")
    ax = fig.add_subplot(111, projection="3d", facecolor="black")

    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    ax.xaxis.pane.set_edgecolor("white")
    ax.yaxis.pane.set_edgecolor("white")
    ax.zaxis.pane.set_edgecolor("white")
    
    ax.tick_params(colors="white")
    ax.w_xaxis.line.set_color("white")
    ax.w_yaxis.line.set_color("white")
    ax.w_zaxis.line.set_color("white")
    
    allX = records[:,:,0].flatten()
    allY = records[:,:,1].flatten()
    allZ = records[:,:,2].flatten()
    ax.set_xlim(allX.min()*0.9, allX.max()*1.1)
    ax.set_ylim(allY.min()*0.9, allY.max()*1.1)
    ax.set_zlim(allZ.min()*0.9, allZ.max()*1.1)
    ax.set_aspect("equal")
    
    # colors = ["yo","co","wo"]
    # points = [ax.plot([], [], c, label=name)[0] for c, name in zip(colors, bodyNames)]

    colors = ["yellow", "cyan", "white"]
    points = [ax.plot([], [], [], 'o', color=c, label=name, markersize=6)[0] for c, name in zip(colors, bodyNames)]
    trails = [ax.plot([], [], [], '-', color=c, linewidth=1, alpha=0.5)[0] for c in colors]

    ax.grid(False)
    
    # Trecho de visualization.py (CORRIGIDO)
    def update(frame, records, points, trails):
        for i, (point, trail) in enumerate(zip(points, trails)):
            # Acessando na ordem correta: [corpo, frame, coordenada]
            point.set_data([records[i, frame, 0]], [records[i, frame, 1]])
            point.set_3d_properties([records[i, frame, 2]])

            trail.set_data(records[i, :frame, 0], records[i, :frame, 1])
            trail.set_3d_properties(records[i, :frame, 2])
        return points + trails
    
    #anim = FuncAnimation(fig, update, frames=N, interval=50, blit=True)
    # Linha CORRIGIDA
    anim = FuncAnimation(fig, update, frames=N, fargs=(records, points, trails), interval=50, blit=True)
    anim.save(outFile, writer="ffmpeg", fps=animationRate)