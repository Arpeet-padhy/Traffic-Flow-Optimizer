# 🚦 Traffic Flow Optimizer

A Python simulation of traffic flow at intersections, using Pandas and NumPy to optimize signal timings based on traffic volume.

## Features
- Simulated traffic data generator
- Optimization logic for signal timing
- Parallel simulation of multiple intersections
- Data analysis and visualization using Pandas

## Future Work
- Integrate RL agent to learn adaptive control
- Real-time dashboard with Streamlit
# Traffic-Flow-Optimizer

# Smart Traffic Signal Optimizer

🚦 **Smart Traffic Signal Optimizer** is a Python-based simulation and optimization system for traffic light scheduling at multiple intersections. It leverages data simulation, multiprocessing, and visualization to demonstrate how traffic signals can be optimized dynamically based on vehicle counts.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How It Works](#how-it-works)
- [Visualizing Results](#visualizing-results)
- [Future Enhancements](#future-enhancements)
- [Author](#author)

---

## Overview

This project simulates traffic data for multiple intersections and optimizes traffic light green times to improve flow. It uses realistic random data generation and parallel processing to handle multiple intersections simultaneously.

The system outputs CSV files representing vehicle counts and optimized green light schedules, which can then be visualized through an interactive dashboard.

---

## Features

- Simulates traffic flow data per intersection with vehicle counts per lane and minute
- Calculates optimized green light durations based on traffic volume
- Parallel processing of multiple intersections to speed up optimization
- Exports data and optimization results to CSV files for analysis
- Interactive Streamlit dashboard for visualization of raw and optimized data

---

## Technologies Used

- **Python 3.8+**
- **Pandas** for data manipulation
- **NumPy** for statistical simulation
- **Multiprocessing** module for parallel execution
- **Streamlit** for creating the interactive web dashboard
- **Matplotlib** for plotting data visualizations

---

## Project Structure

traffic-flow-optimizer/
├── src/
│ ├── generate_multiple.py # Generates simulated traffic data CSVs
│ ├── simulate_all.py # Optimizes green times in parallel
│ └── dashboard.py # Streamlit dashboard for visualization
├── data/
│ ├── traffic_A.csv # Sample traffic data for intersection A
│ ├── traffic_B.csv # Sample traffic data for intersection B
│ ├── traffic_C.csv # Sample traffic data for intersection C
│ ├── optimized_A.csv # Optimized schedule for intersection A
│ ├── optimized_B.csv # Optimized schedule for intersection B
│ └── optimized_C.csv # Optimized schedule for intersection C
└── README.md # Project documentation


---

## Getting Started

### Prerequisites

Make sure you have Python 3.8 or above installed. You can check with:

python --version

Installation
Clone the repository:

git clone https://github.com/your-username/traffic-flow-optimizer.git
cd traffic-flow-optimizer

Install required Python packages:

pip install -r requirements.txt

(If you don’t have requirements.txt, just install manually:)

pip install pandas numpy streamlit matplotlib


How It Works
1. Simulate Traffic Data
Run the data generator to create CSV files simulating traffic counts per lane for each intersection.

python src/generate_multiple.py

2. Optimize Traffic Signals
Run the optimizer that processes the CSVs in parallel and outputs optimized green light durations.
python src/simulate_all.py


3. Visualize Results
Launch the interactive Streamlit dashboard to explore the data and optimization results visually.

streamlit run src/dashboard.py

The dashboard lets you select intersections, view raw traffic counts, and see the optimized green signal schedules with charts.

Visualizing Results
The dashboard displays:

Tables showing raw vehicle counts by direction and time

Bar charts aggregating total vehicle counts per lane

Line charts showing green light durations scheduled for each direction over time

Future Enhancements
Integrate real-world traffic sensor data for live optimization

Implement machine learning models to predict traffic volumes

Add map-based visualization using folium or geopandas

Deploy the dashboard on cloud platforms for public access

Incorporate more advanced optimization algorithms (e.g., reinforcement learning)

Author
Arpeet Padhy
LinkedIn | GitHub | Portfolio

License
This project is licensed under the MIT License.

Feel free to contribute or raise issues!

