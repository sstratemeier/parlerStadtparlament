import logging
import json
import pandas as pd
import numpy as np
import geopandas as gpd
from shapely.geometry import shape
import matplotlib.pyplot as plt
import matplotlib


# Source: https://matplotlib.org/3.1.1/gallery/images_contours_and_fields/image_annotated_heatmap.html
def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw=None, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row_labels
        A list or array of length M with the labels for the rows.
    col_labels
        A list or array of length N with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts


# Function to convert JSON strings to Shapely geometry objects
def json_to_geometry(json_str):
    try:
        json_dict = json.loads(json_str)
        return shape(json_dict)
    except Exception as e:
        print(f"Error converting JSON to geometry: {e}")
        return None

def main():
    df_traktanden = pd.read_excel('data/Daten_mit_Quartier_v2.xlsx')
    # Group by "Quartiere" and Count Occurences of "Quartiere"
    # Also count null as "Keine Quartierangabe"
    df_traktanden['Quartiere'] = df_traktanden['Quartiere'].fillna('Keine Quartierangabe')
    df_quartier = df_traktanden.groupby('Quartiere').size().reset_index(name='count')
    # Sort by count
    df_quartier = df_quartier.sort_values(by=['count'], ascending=False)
    df_wohnviertel = pd.read_csv('data/wohnviertel@stadt-stgallen.csv', sep=';')
    # Merge on "Quartiere"
    df_merged = pd.merge(df_quartier, df_wohnviertel, left_on='Quartiere', right_on='Quartiergruppen')

    df_merged['geometry'] = df_merged['Geo Shape'].apply(json_to_geometry)
    gdf = gpd.GeoDataFrame(df_merged, geometry='geometry')
    fig, ax = plt.subplots(1, 1)
    gdf.plot(column='count', cmap='plasma', legend=True, ax=ax)
    ax.set_title('Heatmap of Quartiere Counts')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    # Saving the plot to a file
    plot_file_path = 'plots/heatmap_quartiere_counts.png'
    plt.savefig(plot_file_path, dpi=300)

    df_person_expanded = df_traktanden.dropna(subset=['Person']).copy()
    df_person_expanded['Person'] = df_person_expanded['Person'].str.split(';')
    df_person_expanded = df_person_expanded.explode('Person')

    # Create datatable and Count occurences of Person (row) per Quartier (column)
    df_person_quartier = pd.crosstab(df_person_expanded['Person'], df_person_expanded['Quartiere'])
    df_person_quartier.to_csv('data/person_quartier.csv')

    ''' TODO: Fix this
    # Plot Heatmap of Person Counts
    fig, ax = plt.subplots()
    im, cbar = heatmap(df_person_quartier.values, df_person_quartier.index, df_person_quartier.columns, ax=ax,
                       cmap="YlGn", cbarlabel="Person Counts")
    texts = annotate_heatmap(im, valfmt="{x:.1f} t")

    fig.tight_layout()
    plt.savefig('plots/heatmap_person_counts.png', dpi=300)

    df_partei_expanded = df_traktanden.dropna(subset=['Partei']).copy()
    df_partei_expanded['Partei'] = df_partei_expanded['Partei'].str.split(';')
    df_partei_expanded = df_partei_expanded.explode('Partei')

    # Create datatable and Count occurences of Partei (row) per Quartier (column)
    df_partei_quartier = pd.crosstab(df_partei_expanded['Partei'], df_partei_expanded['Quartiere'])
    df_partei_quartier.to_csv('data/partei_quartier.csv')

    # Plot Heatmap of Partei Counts
    fig, ax = plt.subplots()

    im, cbar = heatmap(df_partei_quartier.values, df_partei_quartier.index, df_partei_quartier.columns, ax=ax,
                          cmap="YlGn", cbarlabel="Partei Counts")
    texts = annotate_heatmap(im, valfmt="{x:.1f} t")

    fig.tight_layout()
    plt.savefig('plots/heatmap_partei_counts.png', dpi=300)
    '''

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info(f'Executing {__file__}...')
    main()
