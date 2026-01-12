import streamlit as st
import pandas as pd
import joblib
import numpy as np

def prediction_app():
    # Konfigurasi halaman
    st.set_page_config(page_title="Aplikasi Prediksi", layout="centered")

    # Gaya latar belakang dan header

    # Header
    st.markdown("<div class='title-box'><h1>🚕 Taxi Trip Price Prediction</h1></div>", unsafe_allow_html=True)
    st.write("Silahkan isi fitur-fitur berikut untuk memprediksi harga trip taksi:")

    # Load model dan metadata
    model = joblib.load("ridge_regression_model.pkl")
    numerical_cols = joblib.load("numeric_columns.pkl")
    feature_columns = [col for col in numerical_cols if col != "trip_price"]

    # Label ramah pengguna
    label_alias = {
        "Trip_Distance_km": "Jarak Trip (km)",
        "Passenger_Count": "Jumlah Penumpang",
        "Base_Fare": "Tarif Dasar",
        "Per_Km_Rate": "Tarif per Km",
        "Per_Minute_Rate": "Tarif per Menit",
        "Trip_Duration_Minutes": "Durasi Trip (menit)"
    }

    # Input user dalam dua kolom
    input_data = {}
    col1, col2 = st.columns(2)
    for i, col in enumerate(feature_columns):
        label = label_alias.get(col, col)
        with col1 if i % 2 == 0 else col2:
            input_data[col] = st.number_input(f"{label}", value=0.0)

    # Prediksi
    input_df = pd.DataFrame([input_data])
    st.markdown("<div class='predict-button'>", unsafe_allow_html=True)
    if st.button("🔮 Prediksi"):
        prediction = model.predict(input_df)
        st.markdown(f"<div class='prediction-box'><h2>Estimasi Harga Trip:</h2><h1>$ {prediction[0]:,.2f}</h1></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # st.title("Taxi Trip Price Prediction")

    # # 1. Load Model & Metadata    
    # model = joblib.load("ridge_regression_model.pkl")
    # numerical_cols = joblib.load("numeric_columns.pkl") 

    # st.set_page_config(page_title="Aplikasi Prediksi", layout="centered")

    # st.write("Silahkan isi fitur-fitur berikut untuk memprediksi harga trip taksi:")

    # # ❗ EXCLUDE TARGET
    # feature_columns = [col for col in numerical_cols if col != "trip_price"]

    # # 🔤 Label yang lebih ramah pengguna
    # label_alias = {
    #     "Trip_Distance_km": "Jarak Trip (km)",
    #     "Passenger_Count": "Jumlah Penumpang",
    #     "Base_Fare": "Tarif Dasar",
    #     "Per_Km_Rate": "Tarif per Km",
    #     "Per_Minute_Rate": "Tarif per Menit",
    #     "Trip_Duration_Minutes": "Durasi Trip (menit)"
    # }

    # # Input user
    # input_data = {}
    # for col in feature_columns:
    #     label = label_alias.get(col, col)  # fallback ke nama asli jika tidak ada alias
    #     input_data[col] = st.number_input(
    #         f"Masukkan {label}",
    #         value=0.0
    #     )

    # # Convert to DataFrame
    # input_df = pd.DataFrame([input_data])

    # # Prediction
    # if st.button("🔮 Prediksi"):
    #     prediction = model.predict(input_df)
    #     st.success(f"Estimasi Harga Trip: **{prediction[0]:,.2f}**")


# def prediction_app():
#     st.title("Taxi Trip Price Prediction")

#     # 1. Load Model & Metadata    
#     model = joblib.load("ridge_regression_model.pkl")
#     numerical_cols = joblib.load("numeric_columns.pkl") 


#     st.set_page_config(page_title="Aplikasi Prediksi", layout="centered")

#     st.write("Silahkan isi fitur-fitur berikut untuk memprediksi harga trip taksi:")

#     # ❗ EXCLUDE TARGET
#     feature_columns = [col for col in numerical_cols if col != "trip_price"]

#     # Input user
#     input_data = {}
#     for col in feature_columns:
#         input_data[col] = st.number_input(
#             f"Masukkan nilai {col}",
#             value=0.0
#         )

#     # Convert to DataFrame
#     input_df = pd.DataFrame([input_data])

#     # Prediction
#     if st.button("🔮 Prediksi"):
#         prediction = model.predict(input_df)
#         st.success(f"Estimasi Harga Trip: **{prediction[0]:,.2f}**")
