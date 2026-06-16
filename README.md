# RidePulse: Mobility Data Pipeline & Anomaly Detection

## Overview

RidePulse is an end-to-end data analytics project that simulates how a mobility technology company can monitor ride-hailing operations using trip, location, fare, and weather data.

The project focuses on data extraction, SQL analytics, API integration, data quality checks, anomaly detection, and business communication.

## Business Question

How can a mobility platform detect operational anomalies and explain demand changes using trip, fare, location, and weather data?

## Tech Stack

- Python
- SQL
- DuckDB
- pandas
- Parquet
- Open-Meteo API
- Jupyter Notebook
- Streamlit
- pytest

## Data Sources

- NYC Taxi & Limousine Commission Yellow Taxi Trip Records
- NYC Taxi Zone Lookup Table
- Open-Meteo Historical Weather API

## Project Architecture

The project follows a bronze, silver, and gold data architecture:

- Bronze: raw trip and weather data
- Silver: cleaned and standardized data
- Gold: analytics-ready tables for demand, revenue, anomalies, and business insights

## Repository Structure

```text
ridepulse-mobility-data-pipeline/
│
├── README.md
├── requirements.txt
├── .gitignore
├── docker-compose.yml                 # opcional
│
├── data/
│   ├── bronze/                         # datos crudos
│   ├── silver/                         # datos limpios
│   └── gold/                           # tablas analíticas
│
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_anomaly_detection.ipynb
│   └── 03_business_insights.ipynb
│
├── src/
│   ├── ingest_trips.py
│   ├── ingest_weather_api.py
│   ├── clean_trips.py
│   ├── build_features.py
│   ├── detect_anomalies.py
│   └── utils.py
│
├── sql/
│   ├── 01_create_tables.sql
│   ├── 02_quality_checks.sql
│   ├── 03_business_metrics.sql
│   └── 04_root_cause_analysis.sql
│
├── reports/
│   ├── executive_summary.md
│   └── data_quality_report.md
│
├── dashboard/
│   └── app.py                          # Streamlit opcional
│
└── tests/
    ├── test_cleaning.py
    └── test_anomaly_rules.py
```
