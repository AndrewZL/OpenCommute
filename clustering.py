import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist


class cluster():
    def __init__(self, dataframe):
        self.df = dataframe
        self.df_std = StandardScaler().fit_transform(self.df)

    def get_closest_node(self, node, nodes):
        closest_index = cdist(node, self.df).argmin()
        return nodes[closest_index]

    def cluster_euclidian(self, node, nodes):
        distances = cdist(np.array[node], self.df).argpartition(3)
        return distances
