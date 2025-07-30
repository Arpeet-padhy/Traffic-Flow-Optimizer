import pandas as pd
from multiprocessing import Process
import os

def optimize_for_intersection(intersection_id):
    path = f"data/traffic_{intersection_id}.csv"
    df = pd.read_csv(path, parse_dates=["Time"])

    def optimize_green_time(group):
        green_times = {}
        for direction in ['North', 'South', 'East', 'West']:
            count = group[group['Direction'] == direction]['VehicleCount'].sum()
            green_time = min(120, 30 + count // 2)
            green_times[direction] = green_time
        return green_times

    schedule = []
    for time, group in df.groupby('Time'):
        green_times = optimize_green_time(group)
        schedule.append({
            "Time": time,
            **green_times
        })

    result_df = pd.DataFrame(schedule)
    result_df.to_csv(f"data/optimized_{intersection_id}.csv", index=False)
    print(f"✅ Optimized schedule saved for Intersection {intersection_id}")

if __name__ == "__main__":
    processes = []

    for inter_id in ['A', 'B', 'C']:
        p = Process(target=optimize_for_intersection, args=(inter_id,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
