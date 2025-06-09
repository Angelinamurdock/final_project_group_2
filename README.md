# 🏡 Denver Real Estate Forecasting with Machine Learning

**Creators**: Angelina Murdock, Kanchan Kumari, Luke Roberts  
**Date**: June 2025

---

## Overview

This project forecasts housing price trends across Denver neighborhoods through 2035 using time series analysis and machine learning. We implement and compare three models—**Linear Regression**, **Keras (Neural Network)**, and **Facebook Prophet**—to evaluate their forecasting accuracy and performance. The final results are visualized using **Tableau Dashboards** and an interactive **Flask App**.

---

## Table of Contents
- [Research Questions](#research-questions)
- [Features](#features)
- [Deployment](#deployment)
- [Model Optimization](#model-optimization)
- [Key Findings](#key-findings)
- [Recommendations](#recommendations)
- [Methodology](#methodology)
- [Model Comparison](#model-comparison)
- [Ethical Considerations](#ethical-considerations)
- [Opportunities for Further Analysis](#opportunities-for-further-analysis)
- [Resources](#resources)

---

## Research Questions

1. What are the projected home values by neighborhood through 2035?
2. Which forecasting model performs best?
3. Which neighborhoods are expected to experience the highest appreciation?
4. How do predictions differ when using annual vs. quarterly data?

---

## Features

- **Data Cleaning & EDA**: Outlier removal, missing value handling, time formatting, and neighborhood aggregation.
- **Forecasting Models**:
  - **Linear Regression**: Baseline model using annual data by neighborhood.
  - **Keras**: Deep learning models using dense layers for both yearly and quarterly forecasting.
  - **Prophet**: Time series model tuned by neighborhood, capturing seasonality and trend changes.
- **Evaluation Metrics**: MAE, MSE, RMSE, MPE, R².
- **Interactive Tools**:
  - **Tableau Dashboard**: Trend visualizations, geospatial mapping, and comparisons by neighborhood.
  - **Flask App**: Web app for exploring neighborhood-level forecasts.

---

## Deployment

### Local Setup Instructions:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Angelinamurdock/final_project_group_2.git
   cd final_project_group_2

2. **Launch Notebooks:**
    - `linear_regression_model.ipynb` — Linear Regression
    - `keras_model_yearly.ipynb` or `keras_model_quarterly.ipynb` — Keras annual and quarterly models
    - `prophet_model.ipynb` — Facebook Prophet
**3. Run the Flask App locally (optional):**
```bash
python app.py
```
**4. Open the Tableau Workbook:**
- Open `forecast_dashboard.twbx` to interact with visualizations of future housing values.

**Requirements include:**
- Python 3.x
- pandas
- scikit-learn
- jupyter
- TensorFlow / Keras
- prophet
- Jupyter Notebook
- Flask
- Tableau

---

## 🔍 Model Optimization

- **Keras Models**:
  - The **yearly model** achieved **RMSE ≈ $39K**, offering stable long-term forecasting.
  - The **quarterly model** captured short-term fluctuations but had a higher **RMSE ≈ $82K**.

- **Prophet**:
  - Accuracy improved by modeling each neighborhood separately.
  - Reduced **MAPE from 34% to 10%**, significantly improving reliability.
  - Employed **cross-validation** to determine optimal forecast horizon.

---

## Key Findings

- **Keras Quarterly** was the most accurate short-term model with the lowest RMSE (~$39K).
- **Prophet** offered consistent, seasonally-aware long-term forecasts through 2035.
- Neighborhoods like **Skyland**, **Regis**, and **Jefferson Park** are projected to **double in value**.
- All models achieved **R² scores above 0.95**, showing strong prediction strength.

---

## Recommendations

- Use **Keras Quarterly** for near-term investment decisions.
- Leverage **Prophet** for strategic long-term planning.
- Prioritize lower-cost, high-growth neighborhoods for stronger returns.
- Validate predictions with up-to-date market data to avoid overfitting.
- Consider external economic conditions in forecasting decisions.

---

## Methodology

### Data Preparation
- Merged Zillow historical data with Denver neighborhood shapefiles.
- Standardized names and filled missing values.
- Created time series from 2015–2025 for training.

### Model Development

- **Linear Regression**: Modeled neighborhood home prices with basic trend lines.
- **Keras Neural Networks**:
  - Built both annual and quarterly models with dense layers.
  - Used dropout and early stopping to prevent overfitting.
- **Prophet**:
  - Incorporated seasonality and changepoints.
  - Tuned models per neighborhood for improved fit.

### Evaluation Metrics
- **MAE** – Mean Absolute Error  
- **MSE** – Mean Squared Error  
- **RMSE** – Root Mean Squared Error  
- **MPE** – Mean Percentage Error  
- **R²** – Coefficient of Determination

### Visualization
- Exported final predictions and joined them with geographic shapefiles.
- Created Tableau dashboards with filters, tooltips, and map interactivity.

---

## Model Comparison

| Model                  | Complexity | Strengths                                                | Limitations                                                            | Best Use Case                                              |
|------------------------|------------|-----------------------------------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------|
| **Linear Regression**  | Low        | Simple, fast, interpretable                               | Assumes linear growth; misses seasonality and market shifts            | Baseline for trend understanding                            |
| **Keras (Neural Net)** | High       | Models nonlinear patterns and dynamics                    | Requires more data; less interpretability                             | Long-term, data-rich forecasting                            |
| **Prophet**            | Medium     | Seasonality and trend shift modeling                      | Less flexible for unique local effects; assumes additive components   | Mid/long-term forecasts with seasonal variation             |

---

## Ethical Considerations

- Data sourced from public datasets (Zillow, Denver Open Data).
- Intended for education and research, not investment advic
- Avoids promoting gentrification or speculative behavior.

---

## Opportunities for Further Analysis

- Add variables like mortgage rates, inflation, and employment trends.
- Build ROI calculators for rentals or Airbnb investments.
- Forecast rent prices alongside home values.
- Visualize confidence intervals and prediction uncertainty.

---

## Resources
- [Zillow Research Data](https://www.zillow.com/research/data/)  
- [Facebook Prophet](https://facebook.github.io/prophet/)  
- [Keras Documentation](https://keras.io/)  
- [Flask Framework](https://flask.palletsprojects.com/)  
- [Tableau](https://www.tableau.com/)  
- [Denver Open Data](https://www.denvergov.org/OpenData)  
- DU Bootcamp Modules: Utilized challenge files and class materials from the bootcamp.
- [ChatGPT by OpenAI](https://openai.com/chatgpt): Assisted with code explanations and debugging.