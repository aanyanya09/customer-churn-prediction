# 📉 Customer Churn Prediction

A Machine Learning web application that predicts whether a telecom customer is likely to churn using customer demographic and service information.

Built with **Python**, **Scikit-learn**, and **Streamlit**.

---

## 🚀 Live Demo
https://customer-churn-predictiongit-cus4e7cetkutycltuglgyo.streamlit.app/

## 💻 Source Code
GitHub Repository:
https://github.com/aanyanya09/customer-churn-prediction.git

---

## 📌 Project Overview

Customer churn is a major challenge for telecom companies. This project predicts customer churn based on customer information such as contract type, internet service, monthly charges, tenure, and other service-related features.

The application provides:
- Churn prediction
- Churn probability
- Risk level (Low / Moderate / High)
- Customer summary

---

## 📊 Dataset

**IBM Telco Customer Churn Dataset**

Features include:
- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Contract Type
- Monthly Charges
- Total Charges
- Payment Method
- Additional Services

---

## 🤖 Machine Learning Models Used

The following models were trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest ⭐ (Selected Model)
- XGBoost
- CatBoost

Random Forest was selected for deployment because it provided the best balance between accuracy and performance.

---

## 📈 Model Evaluation

Evaluation metrics used:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- CatBoost
- Joblib
- Streamlit

---

## 📂 Project Structure

```
customer-churn-prediction/
│
├── app.py
├── requirements.txt
├── rf_model.pk1
├── rf_column.pk1
├── CustomerChurn.png
├── .streamlit/
│   └── config.toml
└── README.md
```

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/aanyanya09/customer-churn-prediction.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📸 Application Preview

(Add a screenshot of your Streamlit app here)

Example:

![Customer Churn App](CustomerChurn.png)

---

## 👩‍💻 Author

**Aanyanya**

GitHub: https://github.com/aanyanya09

---

## ⭐ If you like this project

Please consider giving this repository a ⭐ on GitHub.
