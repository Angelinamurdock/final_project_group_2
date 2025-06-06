# Denver Real Estate Forecasting with Machine Learning
Creators: Luke Roberts, Kanchan Kumari, Angelina Murdock<br>
Date: June 2025

## Overview
We aim to forecast home values by neighborhood in Denver using time series data. Historic home values are analyzed with three models—**Linear Regression**, **Keras(Neural Network)**, and **Facebook Prophet**—to identify trends and compare performance. The goal is to determine the most accurate model and generate 10-year home value forecasts.


## Table of Contents
- [Features](#features)
- [Deployment](#deployment)
- [Optimization](#optimization)
- [Ethical Considerations](#ethical-considerations)
- [Opportunities for Further Analysis](#opportunities-for-further-analysis)
- [Resources](#resources)

## Features
- **Data Cleaning and EDA:** Handling missing data, outlier removal, format reshaping, and aggregation by neighborhood and time period.
- **Linear Regression Model:** Annual home value forecasting per neighborhood using historical Zillow data.
- **Keras Model:** Both annual and quarterly models to capture long-term trends and short-term volatility.
- **Prophet Model:** Time series forecasting optimized by neighborhood with seasonality and trend shifts.

## Deployment
**Local Setup:**
1. Clone the Repository:
    ```bash
    git clone https://github.com/Angelinamurdock/final_project_group_2.git
    ```
2. Open the Jupyter Notebook files to explore data cleaning and model implementation.
3. Model files:
    - `linear_regression_model.ipynb` — Linear Regression
    - `keras_model_yearly.ipynb` or `keras_model_quarterly.ipynb` — Keras annual and quarterly models
    - `prophet_model.ipynb` — Facebook Prophet

**Requirements include:**
- Python 3.x
- pandas
- scikit-learn
- jupyter
- TensorFlow / Keras
- prophet
- Jupyter Notebook

## Optimization
- Compared **Keras models using quarterly and annual data**:
    - Annual data model provided more stable and accurate long-term forecasts (RMSE ≈ $39K).
    - Quarterly data captured short-term trends but introduced volatility and lower accuracy (RMSE ≈ $82K).
- Forecasting each neighborhood separately with Prophet reduced MAPE from **34% to 10%**, greatly improving accuracy.
- Used **cross-validation** in Prophet model to evaluate optimal forecast horizon and model reliability.

## Ethical Considerations
- Data sourced from publicly available Zillow datasets, used solely for research and public awareness.
- Data cleaning limited to standard preprocessing; no personally identifiable information involved.
- Aim to support responsible real estate investment decisions.

## Opportunities for Further Analysis
- Integrate additional neighborhood features (e.g., crime rates, school quality, amenities).
- Explore other forecasting models or ensemble approaches.
- Implement real-time updating as new data becomes available.

## Resources
- **DU Bootcamp Modules:** Utilized challenge files and class materials from the bootcamp.
- [**Zillow Data**](https://www.zillow.com/research/data/) 
- [**Prophet Documentation**](https://facebook.github.io/prophet/docs/quick_start.html#python-api) 
- **ChatGPT:** Assisted with code explanations and debugging.