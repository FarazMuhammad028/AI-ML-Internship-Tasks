# Task 2: Predict Future Stock Prices (Short-Term)

## 📌 Objective
The objective of this task is to use historical stock market data to predict the
next day’s closing price using machine learning regression models.

---

## 📊 Dataset Used
- **Source:** Yahoo Finance
- **Data Access Method:** `yfinance` Python library
- **Description:**  
  The dataset contains historical stock price data including:
  - Open price
  - High price
  - Low price
  - Close price
  - Trading Volume  

  This data is used to analyze short-term price movement patterns.

---

## 🧹 Data Loading and Preprocessing
- Selected a publicly traded company stock (e.g., Apple or Tesla)
- Fetched historical stock data using the `yfinance` API
- Handled missing values if present
- Created input features using:
  - Open
  - High
  - Low
  - Volume
- Used the next day’s closing price as the target variable

---

## 📈 Exploratory Data Analysis (EDA)
- Visualized historical closing prices
- Analyzed trends and price fluctuations
- Compared actual vs predicted prices using line plots

---

## 🤖 Models Applied
- **Linear Regression**
- **Random Forest Regressor** 

---

## 📐 Model Evaluation
The regression models were evaluated using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Visual comparison of actual vs predicted closing prices

---

## ✅ Key Results and Findings
- Linear Regression provided a strong baseline model
- Random Forest captured non-linear relationships in stock data
- Predictions closely followed actual price trends for short-term forecasting
- Market volatility limits long-term prediction accuracy

---

## 🛠 Tools & Technologies
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- yfinance
- Jupyter Notebook

---

## 📌 Conclusion
This task demonstrates the use of historical stock data and regression models
for short-term price prediction. While machine learning can capture trends,
stock prices remain influenced by market conditions and external factors.

---

## 📎 Submission
This task is part of the AI/ML Internship program.  
The complete implementation and results are available in this GitHub repository.


