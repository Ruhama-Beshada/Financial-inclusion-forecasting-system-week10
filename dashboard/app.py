# app.py
import pandas as pd
import os
from dash import Dash, dcc, html
import plotly.express as px

# --- Paths ---
processed_path = r"C:\Users\ruham\Downloads\financial inclusion forecasting system\Financial-inclusion-forecasting-system-week10\data\processed"
forecast_file = os.path.join(processed_path, "ACC_OWNERSHIP_forecast.xlsx")

# --- Load forecast data ---
df_forecast = pd.read_excel(forecast_file)

# Quick check
print(df_forecast.head())

# --- Initialize Dash app ---
app = Dash(__name__)
app.title = "Financial Inclusion Forecast Dashboard"

# --- Layout ---
app.layout = html.Div([
    html.H1("Financial Inclusion Forecast Dashboard"),
    html.P("This dashboard shows actual vs forecast values for ACC_OWNERSHIP."),

    # Graph
    dcc.Graph(
        id='forecast-graph',
        figure=px.line(
            df_forecast,
            x='observation_date',
            y=['actual', 'forecast'],
            title='Actual vs Forecast for ACC_OWNERSHIP',
            labels={'value': 'Value', 'observation_date': 'Date'}
        )
    )
])

# --- Run the app ---
if __name__ == '__main__':
    app.run(debug=True)
