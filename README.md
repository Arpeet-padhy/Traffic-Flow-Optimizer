# 🚦 Traffic Flow Optimizer

A Python-based simulation and optimization tool to model and improve traffic light scheduling at intersections using synthetic data, parallel processing, and a Streamlit dashboard for visual analysis.

---

## 📌 Overview

The **Traffic Flow Optimizer** simulates traffic conditions at multiple intersections, calculates optimal green light durations based on vehicle flow, and visualizes results through an interactive dashboard.

This project is ideal for showcasing skills in:

- Python (NumPy, Pandas)
- Parallel computing
- Data visualization
- Streamlit web apps
- Traffic systems and signal timing optimization

---

## 🧠 Features

✅ Simulates per-minute traffic data (vehicles/lane/intersection)\
✅ Optimizes traffic signal green times using traffic density\
✅ Runs optimization in parallel using multiprocessing\
✅ Outputs to structured CSV files\
✅ Visualizes data and results in a Streamlit dashboard

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **NumPy** – Data simulation and numeric operations
- **Pandas** – Data manipulation and CSV handling
- **Multiprocessing** – Parallel execution of optimization
- **Streamlit** – Web-based interactive dashboard
- **Matplotlib** – Plots and visual insights

---

## 📂 Project Structure

```
traffic-flow-optimizer/
├── src/
│   ├── generate_multiple.py       # Generate synthetic traffic data
│   ├── simulate_all.py            # Parallel optimization logic
│   └── dashboard.py               # Streamlit dashboard interface
├── data/
│   ├── traffic_[A|B|C].csv        # Simulated traffic data
│   └── optimized_[A|B|C].csv      # Optimized green light durations
├── README.md                      # Documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Arpeet-padhy/Traffic-Flow-Optimizer.git
cd Traffic-Flow-Optimizer
```

### 2. Install dependencies

```bash
pip install pandas numpy streamlit matplotlib
```

### 3. Generate traffic data

```bash
python src/generate_multiple.py
```

### 4. Optimize green light durations

```bash
python src/simulate_all.py
```

### 5. Launch the dashboard

```bash
streamlit run src/dashboard.py
```

---

## 📊 Dashboard Preview

The interactive Streamlit app allows you to:

- Select an intersection
- View raw traffic data
- See optimized green durations per direction
- Analyze visual charts (bar and line plots)

---

## 💡 Future Enhancements

- Integrate live sensor data from IoT or traffic APIs
- Implement ML-based traffic prediction models
- Add map-based visualization using `folium` or `geopandas`
- Deploy dashboard publicly via Streamlit Cloud or Heroku
- Use reinforcement learning for advanced signal control

---

## 👤 Author

**Arpeet Padhy**\
🔗 [GitHub](https://github.com/Arpeet-padhy) | 🌐 Portfolio Coming Soon

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributions Welcome!

If you have suggestions or ideas for improvement, feel free to fork this repository, create a pull request, or open an issue.

