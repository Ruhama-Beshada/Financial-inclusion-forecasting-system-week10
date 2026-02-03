# Financial-inclusion-forecasting-system-week10

## 📌 Project Overview

This project builds a **financial inclusion forecasting system for Ethiopia**.  
It covers the **full data science pipeline** — from raw data ingestion and enrichment to forecasting and an interactive dashboard.

The goal is to help policymakers and analysts **understand trends and predict future financial inclusion indicators** using historical data.

---

## 🧱 Project Folder Structure
ethiopia-fi-forecast/
├── data/
│   ├── raw/                      # Original datasets
│   │   ├── ethiopia_fi_unified_data.xlsx
│   │   ├── Additional Data Points Guide.xlsx
│   │   └── reference_codes.xlsx
│   └── processed/                # Cleaned and enriched datasets + forecast outputs
│       ├── ACC_OWNERSHIP_forecast.xlsx
│       ├── all_aggregated_forecasts.xlsx
│       ├── ethiopia_fi_features.xlsx
│       └── ethiopia_fi_unified_data_enriched.xlsx
├── notebooks/                    # Jupyter notebooks for each task
│   ├── task1_data_exploration.ipynb
│   ├── task2_forecasting.ipynb
│   ├── task3_modeling.ipynb
│   └── task4_analysis.ipynb
├── src/                          # Python helper scripts
│   ├── __init__.py
│   └── data_utils.py
├── reports/
│   └── figures/                  # Visualizations and charts
├── models/                       # Forecasting models (saved if needed)
├── dashboard/                     # Dash interactive dashboard
│   └── app.py
├── tests/
│   └── test_basic.py
├── requirements.txt
├── README.md
└── .gitignore

---

## ⚙️ Environment Setup

### 1️⃣ Create Conda Environment
 bash
conda create -n ethiopia-fi python=3.10 -y
conda activate ethiopia-fi

###  2️⃣ Install Dependencies
pip install -r requirements.txt
# 🧪 Task Breakdown
## ✅ Task 1: Data Exploration & Cleaning

**Location:** `notebooks/task1_data_exploration.ipynb`

**What was done:**

- Loaded raw Excel datasets from `data/raw/`
- Explored:
  - **Record types** (`observation`, `event`, `impact_link`)
  - **Pillars** (`ACCESS`, `USAGE`, etc.)
  - **Indicators and time range**
- Validated data using: `reference_codes.xlsx`
- Enriched data using: `Additional Data Points Guide.xlsx`
- Cleaned data:
  - Converted **dates & numeric values**
  - Removed **duplicates**
  - Handled **missing values**

📁 **Output:**

Cleaned and enriched dataset saved to:  
`data/processed/ethiopia_fi_unified_data_enriched.xlsx`

---

## ✅ Task 2: Feature Engineering

**Location:** `notebooks/task2_feature_engineering.ipynb`

**What was done:**

- Selected **target indicator(s)**
- Aggregated **historical trends**
- Engineered **features for forecasting**
- Prepared **structured time-series data**

📁 **Output:**

`data/processed/ethiopia_fi_features.xlsx`

---

## ✅ Task 3: Forecasting

**Location:** `notebooks/task3_forecasting.ipynb`

**What was done:**

- **Train-test split** on time series data
- Built **forecasting models**
- Generated **future predictions**
- Compared **actual vs forecast values**

📁 **Outputs:**

- `data/processed/ACC_OWNERSHIP_forecast.xlsx`  
- `data/processed/all_aggregated_forecasts.xlsx`

---

## ✅ Task 4: Analysis & Visualization

**Location:** `notebooks/task4_analysis.ipynb`

**What was done:**

- Visualized:
  - **Actual vs forecast trends**
- Generated **forecast plots**
- Saved **figures for reporting**

📁 **Outputs:**

`reports/figures/*.png`

> Optional enhancements (**percentage error, missing months**) were intentionally skipped to proceed to dashboard development.

---

## ✅ Task 5: Interactive Dashboard (Dash)

**Location:** `dashboard/app.py`

**Features:**

- Built using **Dash + Plotly**
- Reads forecast Excel files automatically
- **Dropdown** to select indicators
- Interactive **line chart**: Actual vs Forecast

**Run the Dashboard**
bash
cd dashboard
python app.py

## 🌐 Open in browser:
http://127.0.0.1:8050/

📊 Forecast Files Used by Dashboard
File Name	Description
ACC_OWNERSHIP_forecast.xlsx	Forecast for account ownership
all_aggregated_forecasts.xlsx	Aggregated indicator forecasts
🧠 Key Technologies Used

-Python
-Pandas / NumPy
-Matplotlib / Plotly
-Dash
-Conda
-Jupyter Notebook

# 🚀 Future Improvements

- Add forecast error metrics to dashboard

- Enable multi-indicator comparison

- Add downloadable CSV/Excel exports

- Deploy dashboard online (Render / Heroku)

🏁 Conclusion

This project demonstrates a complete end‑to‑end data science workflow, from raw data to forecasting and deployment.
It is designed to be scalable, reproducible, and decision‑oriented.

👤 Author: Ruham
🎓 Program: Software Engineering / Data Science

