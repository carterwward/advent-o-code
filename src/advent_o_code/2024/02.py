# TODO: Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
import os
import pandas as pd


if __name__ == "__main__":
    filepath = os.path.join("data", "locations.tsv")
    location_df = pd.read_csv(filepath, sep='   ', header=None, index_col=None, engine="python")
    list1_set = set(location_df[0].values)
    list2_counts = location_df[1].value_counts()
    total = 0
    for val1 in list1_set:
        if val1 in list2_counts.index:
            total += val1 * list2_counts.loc[val1]
    print(total)
