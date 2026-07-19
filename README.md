# 🚴 Ford GoBike Data Analysis Dashboard

URL - https://gofordbike-scvm2tt4dtaduccemivtus.streamlit.app/

An interactive **Exploratory Data Analysis (EDA)** dashboard built using **Python** and **Streamlit** to analyze the Ford GoBike bike-sharing dataset. The dashboard provides valuable insights into trip patterns, user demographics, ride durations, and usage trends through interactive visualizations.

---

## 📌 Project Overview

This project analyzes the **Ford GoBike System Data (2018)** to understand customer behavior and identify patterns that can help improve operational efficiency and user experience.

The dashboard allows users to explore the dataset through multiple visualizations and business insights.

---

## 🎯 Business Objective

The objective of this project is to analyze bike-sharing data to:

- Understand customer riding behavior.
- Identify peak usage hours and days.
- Analyze trip duration patterns.
- Compare subscriber and customer usage.
- Discover trends based on age, gender, and stations.
- Provide business recommendations to improve service utilization.

---

## 📊 Features

- Interactive Streamlit Dashboard
- Dataset Overview
- Univariate Analysis
- Bivariate Analysis
- Correlation Heatmap
- Business Insights
- Interactive Charts
- Summary & Recommendations

---

## 📂 Dataset

The project uses the **Ford GoBike Trip Data (2018)** containing monthly trip records.

The repository stores the dataset as monthly ZIP files:

```
201801-fordgobike-tripdata.csv.zip
201802-fordgobike-tripdata.csv.zip
...
201812-fordgobike-tripdata.csv.zip
```

The application automatically reads and combines all monthly datasets during execution.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 📁 Project Structure

```
FordGoBike/
│
├── appp.py
├── EDA.py
├── requirements.txt
├── README.md
│
├── 201801-fordgobike-tripdata.csv.zip
├── 201802-fordgobike-tripdata.csv.zip
├── ...
└── 201812-fordgobike-tripdata.csv.zip
```

---

## ▶️ Run Locally

Clone the repository

```bash
git clone https://github.com/jainoorsingh8-hub/GoFordBike.git
```

Move into the project directory

```bash
cd GoFordBike
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run appp.py
```

---

## 📈 Dashboard Pages

- 🏠 Home
- 📄 Dataset Overview
- 📊 Univariate Analysis
- 📉 Bivariate Analysis
- 🔥 Correlation Analysis
- 💡 Business Recommendations

---

## 📌 Key Insights

- Peak demand occurs during commuting hours.
- Subscribers contribute the majority of trips.
- Most rides are short in duration.
- Weekdays experience higher bike usage than weekends.
- Certain stations consistently record higher traffic.
- User demographics reveal distinct riding patterns.

---

## 🚀 Future Enhancements

- Interactive filters
- Station-wise analysis
- Geographic visualizations
- Predictive demand forecasting
- Real-time dashboard updates

---

## 👨‍💻 Author

**Jainoor Singh Saini**

Computer Science Engineering  
Chandigarh University
