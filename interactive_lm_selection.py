'''
This is an interactive tool for selecting corresponding landmarks between two spatial transcriptomics slices, taking hepatic lobule data as an example.
'''
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import math
import torch
import matplotlib.pyplot as plt
import scanpy as sc
import squidpy as sq
import anndata as ad
import pandas as pd
import anndata
from sklearn.cluster import KMeans
from scipy.spatial import ConvexHull, Delaunay
from ariel_srt.Landmark import normalization_spatial, alternative_landmark
from functools import partial
from matplotlib.patches import Circle
from matplotlib.widgets import Button
import sys
import ipywidgets as widgets
from IPython.display import display

path = '../data/hepatic lobule'

# Take slice1 and slice2 as an example(slice1 as the reference)
for i in range(1,3):
    globals()[f"data_slice{i}"]=sc.read_h5ad(f'{path}/data_slice{i}.h5ad')

spatial1 = normalization_spatial(data_slice1.obsm['spatial'])
data_slice1.obsm['spatial'] = spatial1

for i in range(2,3):  #(2,11)
    globals()[f'lm1_{i}'], globals()[f'lm{i}'] = alternative_landmark(spatial1, globals()[f"data_slice{i}"].obsm['spatial'], data_slice1.obsm['pca'], globals()[f"data_slice{i}"].obsm['pca'], n = 100)

spatial1 = normalization_spatial(data_slice1.obsm['spatial']) 
spatial2 = data_slice2.obsm['spatial']
landmark1 = lm1_2[range(50),:]
landmark2 = lm2[range(50),:]


highlights = []
highlight_history = []  

def _radius(ax, scale=0.03):
    x0, x1 = ax.get_xlim(); y0, y1 = ax.get_ylim()
    return scale * max(abs(x1-x0), abs(y1-y0))

def on_pick(event, lm1, lm2, spatial1, spatial2):
    global highlights, highlight_history

    # Only respond to picks on landmark scatter plots
    if event.artist not in (scatter2, scatter4):
        return

    indices = np.atleast_1d(event.ind).astype(int)
    xdata, ydata = event.artist.get_offsets().T

    r1 = _radius(ax1)
    r2 = _radius(ax2)

    for idx in indices:
        j = int(idx)

        sel1 = ax1.scatter([lm1[j, 0]], [lm1[j, 1]],
                           s=ring_size.value, facecolors='none',
                           edgecolors='black', linewidths=2, zorder=6)
        sel2 = ax2.scatter([lm2[j, 0]], [lm2[j, 1]],
                           s=ring_size.value, facecolors='none',
                           edgecolors='black', linewidths=2, zorder=6)
        
        highlights.extend([sel1, sel2])
        highlight_history.append((sel1, sel2))

        if event.artist == scatter2:
            print(f"Lm1 at ({xdata[idx]:.6f}, {ydata[idx]:.6f}) with index: [{idx}]")
            print(f"Corresponding Lm2 at({lm2[idx, 0]:.6f}, {lm2[idx, 1]:.6f})")
        else:
            print(f"Lm2 at ({xdata[idx]:.6f}, {ydata[idx]:.6f}) with index: [{idx}]")
            print(f"Corresponding Lm1 at({lm1[idx, 0]:.6f}, {lm1[idx, 1]:.6f})")

    fig.canvas.draw_idle()

    print("Selected indices:", indices.tolist())
    sys.stdout.flush()  

def clear_highlights(event):
    global highlights, highlight_history
    while highlights:
        highlights.pop().remove()
    highlight_history.clear()
    fig.canvas.draw_idle()
    print("All highlights cleared."); sys.stdout.flush()

def undo_highlight(event):
    global highlights, highlight_history
    if highlight_history:
        c1, c2 = highlight_history.pop()
        if c2 in highlights: highlights.remove(c2)
        if c1 in highlights: highlights.remove(c1)
        c1.remove(); c2.remove()
        fig.canvas.draw_idle()
        print("Last highlight pair undone."); sys.stdout.flush()
    else:
        print("Nothing to undo."); sys.stdout.flush()

def save_figure(event):
    fig.savefig('highlighted_figure.png', dpi=300, bbox_inches='tight')
    print("Figure saved as 'highlighted_figure.png'."); sys.stdout.flush()




# Set highlighting ring size
ring_size = widgets.IntSlider(value=250, min=50, max=1200, step=25, description='Ring size')
display(ring_size)

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, dpi=150, figsize=(15, 8))

# Background data points
ax1.scatter(spatial1[:, 0], spatial1[:, 1], s=1)
ax2.scatter(spatial2[:, 0], spatial2[:, 1], s=1)

# Pickable landmarks
scatter2 = ax1.scatter(landmark1[:, 0], landmark1[:, 1], s=25, c="red", picker=5, zorder=3)
scatter4 = ax2.scatter(landmark2[:, 0], landmark2[:, 1], s=25, c="red", picker=5, zorder=3)

# Labels with indices
for i in range(landmark1.shape[0]):
    ax1.text(landmark1[i, 0], landmark1[i, 1], f'{i}', c='red', fontsize=7)
for i in range(landmark2.shape[0]):
    ax2.text(landmark2[i, 0], landmark2[i, 1], f'{i}', c='red', fontsize=7)

#ax1.invert_yaxis(); ax1.invert_xaxis()
#ax2.invert_yaxis(); ax2.invert_xaxis()
ax1.set_title('slice1', fontsize=20)
ax2.set_title('slice2', fontsize=20)

# Connect pick event
on_pick_with_lm = partial(on_pick, lm1=landmark1, lm2=landmark2, spatial1=spatial1, spatial2=spatial2)
pick_id = fig.canvas.mpl_connect('pick_event', on_pick_with_lm)

# Buttons
clear_button_ax = plt.axes([0.9, 0.15, 0.1, 0.05])
clear_button = Button(clear_button_ax, 'Clear Highlights', hovercolor='0.9')
clear_button.label.set_fontsize(7)
clear_button.on_clicked(clear_highlights)

undo_button_ax = plt.axes([0.9, 0.2, 0.1, 0.05])
undo_button = Button(undo_button_ax, 'Undo Highlights', hovercolor='0.9')
undo_button.label.set_fontsize(7)
undo_button.on_clicked(undo_highlight)

save_button_ax = plt.axes([0.9, 0.25, 0.1, 0.05])
save_button = Button(save_button_ax, 'Save Figure', hovercolor='0.9')
save_button.label.set_fontsize(8)
save_button.on_clicked(save_figure)

plt.show()