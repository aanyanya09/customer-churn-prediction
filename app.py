import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.set_page_config(page_title="CUSTOMER CHURN PREDICTION", page_icon="📉",
    layout="wide",
    initial_sidebar_state=400)
st.image("CustomerChurn.png", width=400)
st.sidebar.title("📘 About")

st.sidebar.info("""
**Customer Churn Prediction App**

📌 Model: Random Forest

📊 Dataset: IBM Telco Customer Churn

🛠 Developed using:
- Python
- Scikit-learn
- Streamlit
""")
@st.cache_resource
def load_model():
    model = joblib.load("rf_model.pk1")
    columns = joblib.load("rf_column.pk1")
    return model, columns

model, columns = load_model()
st.title("📉 Customer Churn Prediction")
st.markdown(
    "Fill in the customer's information below and click **Predict Churn**."
)


with st.expander("📋 Customer Details", expanded=True):

 col1, col2 = st.columns([1, 1])

 with col1:
    gender=st.selectbox("Gender",["Female","Male"])
    senior=st.selectbox("senior citizen",["No","Yes"])
    partner=st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])
    tenure = st.slider("Tenure", 0, 72, 12)
    phone_service=st.selectbox("phone service",["No","Yes"])
    Multiple_lines=st.selectbox("Multiple lines",["No","Yes","No phone service"])
    internet_service=st.selectbox("internet service",["DSL","Fiber optic","No"])
    online_security=st.selectbox("online security",["No","Yes","No internet service"])
    online_backup=st.selectbox("online backup",["No","Yes","No internet service"])

 with col2:
    contract = st.selectbox("Contract",["Month-to-month", "One year", "Two year"])
    monthly_charges = st.number_input("Monthly Charges",min_value=0.0)
    total_charges = st.number_input("Total Charges",min_value=0.0)
    Device_Protection=st.selectbox("Device Protection",["No","Yes","No internet service"])
    Tech_Support=st.selectbox("Tech Support",["No","Yes","No internet service"])
    Streaming_TV=st.selectbox("Streaming TV",["No","Yes","No internet service"])
    Streaming_Movies=st.selectbox("Streaming Movies",["No","Yes","No internet service"])
    Paperless_Billing=st.selectbox("Paperless Billing",["No","Yes"])
    Payment_Method=st.selectbox("Payment Method",["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"])


if st.button("Predict Churn", type="primary"):
    # Convert Yes/No columns to 0/1
    raw = pd.DataFrame([{
    "gender": gender,
    "SeniorCitizen": 1 if senior == "Yes" else 0,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone_service,
    "MultipleLines": Multiple_lines,
    "InternetService": internet_service,
    "OnlineSecurity": online_security,
    "OnlineBackup": online_backup,
    "DeviceProtection": Device_Protection,
    "TechSupport": Tech_Support,
    "StreamingTV": Streaming_TV,
    "StreamingMovies": Streaming_Movies,
    "Contract": contract,
    "PaperlessBilling": Paperless_Billing,
    "PaymentMethod": Payment_Method,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges
    }])
    for col in ["Partner", "Dependents", "PhoneService", "PaperlessBilling"]:
      raw[col] = raw[col].map({"No": 0, "Yes": 1})

    raw = pd.get_dummies(raw,columns=["Contract", "InternetService", "PaymentMethod"],dtype=int)

    raw = pd.get_dummies(raw,
    columns=[
        "gender",
        "MultipleLines",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies"
    ],
    drop_first=True,
    dtype=int)


    raw["AvgMonthlySpend"] = raw["TotalCharges"] / (raw["tenure"] + 1)
    raw["LongTermCustomer"] = (raw["tenure"] >= 24).astype(int)
    raw["HighMonthlyCharge"] = (raw["MonthlyCharges"] > 80).astype(int)
    service_cols = [
    "OnlineSecurity_Yes",
    "OnlineBackup_Yes",
    "DeviceProtection_Yes",
    "TechSupport_Yes",
    "StreamingTV_Yes",
    "StreamingMovies_Yes"]
    for col in service_cols:
       if col not in raw.columns:
        raw[col] = 0
    raw["TotalServices"] = raw[service_cols].sum(axis=1)


    raw = raw.reindex(columns=columns, fill_value=0)
    pred = model.predict(raw)[0]
    proba = model.predict_proba(raw)[0][1]

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
      st.metric("Prediction", "Likely to churn"if pred == 1 else "Likely to stay")

    with c2:
      st.metric("Probability", f"{proba:.1%}")

    with c3:
      if proba >= 0.75:
        st.warning("🔴 High Risk Customer")

      elif proba >= 0.40:
        st.info("🟠 Moderate Risk Customer")

      else:
        st.success("🟢 Low Risk Customer")
    
    st.subheader("Result")

    if pred == 1:
       st.error(f"⚠️ Likely to churn - Probability: {proba:.1%}")

    else:
       st.success(f"✅ Likely to stay - Probability: {proba:.1%}")
    

    st.metric(
    label="📊 Churn Probability",
    value=f"{proba:.1%}"
    )

    st.progress(min(max(proba,0.0),1.0))
    st.progress(min(max(proba,0.0),1.0))

    chart = pd.DataFrame({
    "Category": ["Stay", "Churn"],
    "Probability": [1-proba, proba]
    })

    st.subheader("📊 Prediction Probability")
    st.bar_chart(chart.set_index("Category"))
    st.balloons()
    summary = pd.DataFrame({
    "Feature": [
        "Gender",
        "Tenure",
        "Contract",
        "Monthly Charges",
        "Total Charges"
    ],
    "Value": [
        gender,
        tenure,
        contract,
        f"${monthly_charges:.2f}",
        f"${total_charges:.2f}"
    ]
    })

    st.subheader("📋 Customer Summary")
    st.table(summary)
    
    