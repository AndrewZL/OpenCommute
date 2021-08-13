import numpy as np
import pandas as pd
from sklearn.neighbors import KernelDensity
import streamlit as st
import pydeck as pdk

from datetime import datetime

inj = pd.read_csv('Data/KSI_CLEAN2.csv')
init_pos = [np.average(inj["LATITUDE"]), np.average(inj["LONGITUDE"])]

vol = pd.read_csv('Data/raw/Cyclist_Volume_Data/CVD-NoTrails.csv')

# Max/Min Lat and Longs
# 43.59204825
# 43.85544546
# -79.63839029
# -79.12589655

latlon = np.vstack([vol['Lat'], vol['Long']]).T

xy = np.random.rand(len(latlon), 2)
xy[:, 0] *= (43.85544546-43.59204825)
xy[:, 0] += 43.59204825
xy[:, 1] *= (-79.63839029+79.12589655)
xy[:, 1] += -79.12589655

kde = KernelDensity(bandwidth=0.01, metric='haversine')
kde.fit(latlon)

z = np.exp(kde.score_samples(xy))
z = z.reshape(len(xy), 1)

vol['x'] = xy[:, 0]
vol['y'] = xy[:, 1]
vol['z'] = z

cur_time = datetime.now().hour

st.write("# Complete Injury Data")
st.write(
    pdk.Deck(
    map_style="mapbox://styles/mapbox/streets-v8",
    initial_view_state={
        "latitude": init_pos[0],
        "longitude": init_pos[1],
        "zoom": 11,
        "pitch": 50,
    },
    layers=[
        pdk.Layer(
            "HeatmapLayer",
            data=inj[['LATITUDE', 'LONGITUDE']],
            get_position=["LONGITUDE", "LATITUDE"],
            opacity=0.9
        ),
    ],
    )
)

st.write("# Complete Volume Data")
st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/streets-v8",
    initial_view_state={
        "latitude": init_pos[0],
        "longitude": init_pos[1],
        "zoom": 11,
        "pitch": 50,
    },
    layers=[
        pdk.Layer(
            "HeatmapLayer",
            data=vol[['Lat', 'Long', 'Volume']],
            get_position=["Long", "Lat"],
            get_weight=["Volume"],
            opacity=0.9
        ),
    ],
))
st.write("# Volume KDE")
st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/streets-v8",
    initial_view_state={
        "latitude": init_pos[0],
        "longitude": init_pos[1],
        "zoom": 11,
        "pitch": 50,
    },
    layers=[
        pdk.Layer(
            "HeatmapLayer",
            data=vol[['x', 'y', 'z']],
            get_position=['y', 'x'],
            get_weight=['z'],
            opacity=0.9
        ),
    ],
))
#
st.write("# Hourly Data")
# Todo: Convert Data to 24 Hour
hour_to_filter = st.slider('Hour', 0, 23, cur_time, key=0)
hour_data = inj[inj['HOUR'] == hour_to_filter]

st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/streets-v8",
    initial_view_state={
        "latitude": init_pos[0],
        "longitude": init_pos[1],
        "zoom": 11,
        "pitch": 50,
    },
    layers=[
        pdk.Layer(
            "HeatmapLayer",
            data=hour_data[['LATITUDE', 'LONGITUDE']],
            get_position=["LONGITUDE", "LATITUDE"],
            opacity=0.9,
        ),
    ],
))  

st.write("# Volume Hourly Data")
hour_to_filter_vol = st.slider('Hour', 0, 23, cur_time)
hour_data_vol = vol[vol['Hour'] == str(hour_to_filter_vol)]

st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/streets-v8",
    initial_view_state={
        "latitude": init_pos[0],
        "longitude": init_pos[1],
        "zoom": 11,
        "pitch": 50,
    },
    layers=[
        pdk.Layer(
            "HeatmapLayer",
            data=hour_data_vol[['Lat', 'Long', 'Volume']],
            get_position=['Long', 'Lat'],
            get_weight=['Volume']
        ),
    ],
))
