import pandas as pd
import numpy as np
import os

def simulate_traffic(intersection_id):
    times = pd.date_range("2023-07-30 08:00", "2023-07-30 10:00", freq="1min")
    lanes = ['North', 'South', 'East', 'West']
    data = []

    for t in times:
        for l in lanes:
            lam = np.random.randint(20, 50)
            count = np.random.poisson(lam=lam)
            data.append([t, l, count])

    df = pd.DataFrame(data, columns=["Time", "Direction", "VehicleCount"])
    df.to_csv(f"data/traffic_{intersection_id}.csv", index=False)
    print(f"✅ Data generated for Intersection {intersection_id}")

if __name__ == "__main__":
    for i in ['A', 'B', 'C']:
        simulate_traffic(i)
