# Inspired by https://juanitorduz.github.io/germany_plots/

import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plotCities(ax,cities):
    for c in cities.index:
        # Plot city name.
        ax.text(
            x=cities['lon'][c], 
            # Add small shift to avoid overlap with point.
            y=cities['lat'][c] + 0.08, 
            s=cities['Name'][c], 
            fontsize=12,
            ha='center', 
        )
        # Plot city location centroid.
        ax.plot(
            cities['lon'][c], 
            cities['lat'][c], 
            marker='o',
            c='black', 
            alpha=0.5
        )


def plotNetwork(ax,cities):
    for f in np.arange(0,cities.shape[0]):
        for t in np.arange(f,cities.shape[0]):
            ax.plot(cities['lon'].iloc[[f,t]],cities['lat'].iloc[[f,t]],c='black',alpha=0.1)

def plotCentralNetwork(ax,cities):
    center = (cities['lon'].mean(),cities['lat'].mean())
    for f in np.arange(0,cities.shape[0]):
        ax.plot([cities['lon'].iloc[f],center[0]],[cities['lat'].iloc[f],center[1]],c='black',alpha=0.1)

if __name__ == '__main__':
    # Load shapes
    plz_shape_df = gpd.read_file('./Data/plz-5stellig.shp', dtype={'plz': str})
    # Load labs and locations
    labs = pd.read_csv('labs.csv')

    fig, ax = plt.subplots(figsize=(8,9))
    plz_shape_df.plot(ax=ax, color='orange', alpha=0.8)
    plotCities(ax,labs)
    # Make pretty
    ax.set(
        title='BCI-Netzwerk', 
        aspect=1.3, 
        facecolor='white'
    );
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    # Saving
    plt.tight_layout()
    plt.savefig('network.png',dpi=600)
    plotCentralNetwork(ax,labs)
    #plotNetwork(ax,labs)
    plt.savefig('network_center_lines.png',dpi=600)
    plt.show()