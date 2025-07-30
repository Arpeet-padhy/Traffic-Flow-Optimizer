import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Traffic Optimizer Dashboard", layout="centered")

st.title("🚦 Smart Traffic Signal Optimizer")
st.markdown("Visualize simulated traffic data and optimized signal schedules.")

# Select intersection
intersection = st.selectbox("Select Intersection", ["A", "B", "C"])

# Load files
traffic_path = f"data/traffic_{intersection}.csv"
optimized_path = f"data/optimized_{intersection}.csv"

@st.cache_data
def load_data():
    traffic_df = pd.read_csv(traffic_path, parse_dates=["Time"])
    opt_df = pd.read_csv(optimized_path, parse_dates=["Time"])
    return traffic_df, opt_df

traffic_df, opt_df = load_data()

st.subheader(f"📈 Vehicle Counts at Intersection {intersection}")
st.dataframe(traffic_df.head(10))

# Aggregate and plot traffic flow
st.markdown("#### Total Vehicle Count per Direction")
agg = traffic_df.groupby("Direction")["VehicleCount"].sum()
st.bar_chart(agg)

st.subheader(f"✅ Optimized Green Times for {intersection}")
st.dataframe(opt_df.head(10))

# Plot green time over time
st.markdown("#### Green Time Schedule (Line Chart)")
fig, ax = plt.subplots()
for d in ["North", "South", "East", "West"]:
    ax.plot(opt_df["Time"], opt_df[d], label=d)
ax.set_xlabel("Time")
ax.set_ylabel("Green Time (sec)")
ax.set_title(f"Green Time per Direction - Intersection {intersection}")
ax.legend()
st.pyplot(fig)
