import pandas as pd
# import numpy as np

df4 = pd.read_csv("./input/OD_2019-04.csv")
stations = pd.read_csv("./input/Stations_2019.csv")


# Quels sont les stations où il y a le plus de départs ?
print(df4.groupby('start_station_code').sum())
