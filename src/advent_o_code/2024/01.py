import os
import pandas as pd


if __name__ == "__main__":
    filepath = os.path.join("data", "locations.tsv")
    location_df = pd.read_csv(filepath, sep='   ', header=None, index_col=None, engine="python")
    list1 = location_df[0].values
    list2 = location_df[1].values
    list1.sort()
    list2.sort()
    total_distance = 0
    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])
    print(total_distance)
