import pandas as pd
import os

# The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

#     The levels are either all increasing or all decreasing.
#     Any two adjacent levels differ by at least one and at most three.



if __name__ == "__main__":
    filepath = os.path.join("data", "reports.tsv")
    with open(filepath, "r") as file:
        lines = file.readlines()
    safe_count = 0
    for report in lines:
        observations = report.strip().split(" ")
        previous_observation = None
        previous_move = None
        safe = True
        for observation in observations:
            if not safe:
                continue

            observation = int(observation)
            if previous_observation is None:
                previous_observation = observation
                continue

            delta = observation - previous_observation
            if abs(delta) > 3 or abs(delta) == 0:
                safe = False
                continue
            if (delta > 0 and previous_move == "negative") or \
                (delta < 0 and previous_move == "positive"):
                safe = False
                continue
            
            if delta > 0:
                previous_move = "positive"
            elif delta < 0:
                previous_move = "negative"
            previous_observation = observation
                
        if safe:
            print(observations)
            safe_count += 1
    print(safe_count)