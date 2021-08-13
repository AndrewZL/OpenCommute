import numpy as np
import pandas as pd
from sklearn.neighbors import KernelDensity


class VolumeData:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        self.init_pos = [np.average(self.df["Lat"]), np.average(self.df["Long"])]
        self.location = 'Toronto'
        self.date_range = [2007, 2017]

    def kde_interpolate(self, min_lat=43.85544546, max_lat=43.59204825, min_lon=-79.63839029, max_lon=79.12589655):
        """
        Interpolates data using kernel density estimation
        :return: volume data after KDE interpolation
        """

        lat_lon = np.vstack([self.df['Lat'], self.df['Long']]).T

        xy = np.random.rand(len(lat_lon), 2)
        xy[:, 0] *= (43.85544546 - 43.59204825)
        xy[:, 0] += 43.59204825
        xy[:, 1] *= (-79.63839029 + 79.12589655)
        xy[:, 1] += -79.12589655

        kde = KernelDensity(bandwidth=0.01, metric='haversine')
        kde.fit(lat_lon)

        z = np.exp(kde.score_samples(xy))
        z = z.reshape(len(xy), 1)

        self.df['x'] = xy[:, 0]
        self.df['y'] = xy[:, 1]
        self.df['z'] = z

        return self.df


class InjuryData:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        self.init_pos = [np.average(self.df["LATITUDE"]), np.average(self.df["LONGITUDE"])]
        self.location = 'Toronto'
        self.date_range = [2007, 2017]