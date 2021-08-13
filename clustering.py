import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


class cluster():
    def __init__(self, dataframe):
        self.df = dataframe
        self.df_std = StandardScaler().fit_transform(self.df)
