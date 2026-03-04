# 📊 Telecom Customer Churn Predictor

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)

## 📌 Overview
Customer retention is crucial for telecommunication companies. This End-to-End Machine Learning project is designed to predict whether an ISP (Internet Service Provider) customer will churn (leave for a competitor) based on their billing details, contract type, and technical support history.

By identifying high-risk customers, companies can proactively offer targeted discounts and retention strategies, effectively saving revenue.

**Live Demo:** [Click here to view the AI Dashboard]([BURAYA SİTENİN LİNKİNİ YAPIŞTIR])

## ⚙️ Features
* **Synthetic Data Generation:** Simulates a realistic ISP customer database with 3,000 records (`data_generator.py`).
* **Machine Learning Model:** Utilizes `scikit-learn`'s Random Forest Classifier with balanced class weights to accurately catch minority churn events (`model_trainer.py`).
* **Interactive Dashboard:** A business-ready web interface built with `streamlit` for instant risk assessment (`app.py`).

## 🛠️ Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas
* **Machine Learning:** Scikit-Learn
* **Model Serialization:** Joblib
* **Web Framework:** Streamlit

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/CanCansas/churn-predictor.git](https://github.com/CanCansas/churn-predictor.git)