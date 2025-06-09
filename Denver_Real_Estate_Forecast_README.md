
# Denver Real Estate Forecasting with Machine Learning
**Creators**: Angelina Murdock, Kanchan Kumari, Luke Roberts  
**Date**: June 2025

## Table of Contents
- [Project Description](#project-description)
- [Research Questions](#research-questions)
- [Features](#features)
- [Deployment](#deployment)
- [Key Findings](#key-findings)
- [Recommendations](#recommendations)
- [Methodology](#methodology)
- [Ethical Considerations](#ethical-considerations)
- [Opportunities for Further Analysis](#opportunities-for-further-analysis)
- [Resources](#resources)

---

## Project Description
This project explores housing price trends across Denver neighborhoods using a combination of historical data and forecasting models. The goal is to analyze future home values through 2035 using multiple models, evaluate their accuracy, and visualize the results through an interactive Tableau dashboard and map as well as a Flask App.

---

## Research Questions
1. What are the projected home values by neighborhood through 2035?
2. Which forecasting model performs best in predicting future prices?
3. Which neighborhoods show the greatest percentage increase in home value?
4. How do forecasted prices compare across quarterly vs. annual trends?

---

## Features
- **Forecasting Models:** Includes Prophet, Linear Regression, and Keras-based deep learning models (quarterly and yearly).
- **Error Metrics:** Model performance compared using MAE, MSE, RMSE, MPE, and R².
- **Interactive Tableau Dashboards:** Forecast trends, neighborhood value comparisons, and geospatial mapping.
- **Flask Application:** For interactive deployment and neighborhood lookups.
- **Data Integration:** Shapefiles and forecast outputs joined for Tableau mapping.

---

## Deployment

### Local Deployment Steps

**1. Clone the Repository:**
```bash
git clone https://github.com/Angelinamurdock/final_project_group_2.git
```

**2. Navigate to the project folder:**
```bash
cd final_project_group_2
```

**3. Launch the Jupyter Notebook to explore modeling and predictions:**
```bash
jupyter notebook
```

**4. Run the Flask App locally (optional):**
```bash
python app.py
```

**5. Open the Tableau Workbook:**
- Open `forecast_dashboard.twbx` to interact with visualizations of future housing values.

---

## Key Findings
- The **Keras Quarterly** model achieved the lowest RMSE (~39,000), indicating highly accurate short-term forecasting.
- The **Prophet** model provided stable long-term predictions, especially useful for trends extending to 2035.
- High-growth neighborhoods like **Skyland**, **Regis**, and **Jefferson Park** are projected to more than **double** in home value.
- R² scores for all models were consistently above **0.95**, demonstrating strong predictive performance.

---

## Recommendations
- Use **Keras Quarterly** for near-term projections and **Prophet** for long-term strategic planning.
- Prioritize investment in high-growth, lower-cost neighborhoods where appreciation potential is high.
- Validate results with additional market data before making financial decisions.
- Avoid overfitting by comparing multiple models and accounting for broader economic conditions.

---

## Methodology

### Data Cleaning & Preparation
- Combined Zillow historical pricing with neighborhood shapefiles.
- Resolved name mismatches across datasets and handled missing values.
- Created consistent time series for each neighborhood from 2015–2025 for training.

### Model Development
- **Keras Neural Networks**:
  - Annual and quarterly models trained using dense layers and ReLU activation.
  - Early stopping and dropout used to prevent overfitting.
- **Prophet**:
  - Applied additive seasonality and changepoints to fit neighborhood-level time series.
- **Linear Regression**:
  - Modeled year and neighborhood interaction using basic trend lines.

### Model Evaluation
- All models evaluated using:
  - **Mean Absolute Error (MAE)**
  - **Mean Squared Error (MSE)**
  - **Root Mean Squared Error (RMSE)**
  - **Mean Percentage Error (MPE)**
  - **R-squared (R²)**

### Visualization
- Final predictions exported and joined with shapefiles for Tableau mapping.
- Custom tooltips, filters, and highlight actions added for interactivity.

---

## Ethical Considerations
All data is sourced from public platforms including Zillow and the City of Denver. This analysis is for educational purposes only and does not constitute investment advice. Care was taken to avoid promoting speculative or gentrifying investment behavior that could harm local communities.

---

## Opportunities for Further Analysis
- Add economic indicators like mortgage rates, inflation, and employment data.
- Build ROI calculators comparing forecasted home value vs. rental income.
- Develop predictive models for rent prices or Airbnb revenue.
- Include prediction intervals and confidence scoring in visualizations.

---

## Resources
- [Zillow Research Data](https://www.zillow.com/research/data/)
- [Facebook Prophet](https://facebook.github.io/prophet/)
- [Keras Documentation](https://keras.io/)
- [Tableau](https://www.tableau.com/)
- [Flask Framework](https://flask.palletsprojects.com/)
- [Denver Open Data](https://www.denvergov.org/OpenData)
- [ChatGPT by OpenAI](https://openai.com/chatgpt)
