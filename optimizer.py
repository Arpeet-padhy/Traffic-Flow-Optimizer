import pandas as pd

def load_traffic_data(path):
    return pd.read_csv(path, parse_dates=["Time"])

def optimize_green_time(group):
    green_times = {}
    for direction in ['North', 'South', 'East', 'West']:
        count = group[group['Direction'] == direction]['VehicleCount'].sum()
        green_time = min(120, 30 + count // 2)
        green_times[direction] = green_time
    return green_times

def generate_schedule(df):
    schedule = []
    for time, group in df.groupby('Time'):
        green_times = optimize_green_time(group)
        schedule.append({
            "Time": time,
            **green_times
        })
    return pd.DataFrame(schedule)

if __name__ == "__main__":
    df = load_traffic_data("data/traffic_data.csv")
    schedule_df = generate_schedule(df)
    schedule_df.to_csv("data/optimized_schedule.csv", index=False)
    print("✅ Optimization complete. Schedule saved to data/optimized_schedule.csv")
