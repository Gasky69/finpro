import pandas as pd
import streamlit as st
import about_dataset
import Vizz
import Prediction_App
import machine_learning

# =========================
# PAGE CONFIG
# =========================
st.set_page_config()
st.markdown("""
<style>
.title-box {
    background: linear-gradient(90deg, #FFD700 0%, #f8b500 100%);
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    animation: fadeIn 2s;
}
.title-box:hover {
    transform: scale(1.05);
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}
.title-text {
    color: #000000;
    font-size: 36px;
    font-weight: bold;
    margin: 0;
}
.subtitle-text {
    font-size: 18px;
    color: #333333;
    margin: 0;
}
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>

<div class="title-box">
    <h1 class="title-text">🚕 Taxi Trip Price Analysis & Prediction</h1>
    <p class="subtitle-text">Analisis data perjalanan taksi dan prediksi harga menggunakan Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# =========================
# CUSTOM BACKGROUND STYLE
# =========================
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #fceabb 0%, #f8b500 100%);
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #2193b0 0%, #6dd5ed 100%);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.title("🚕 Taxi Price App")
    st.markdown("""
    **Final Project – Data Science**  
    **Author:** Albertus Raditya Bagas Primaradi  
    📍 Jakarta, 1 Januari 2026
    """)
    st.divider()
    st.info("Gunakan tab di atas untuk menjelajahi dataset, dashboard, dan prediksi harga.")

# HEADER
# =========================
# st.markdown(
#     """
#     <h1 style='text-align: center;'>🚕 Taxi Trip Price Analysis & Prediction</h1>
#     <p style='text-align: center; font-size:18px;'>
#     Analisis data perjalanan taksi dan prediksi harga menggunakan Machine Learning
#     </p>
#     """,
#     unsafe_allow_html=True
# )


# =========================
# TABS

# Inject custom CSS for tab animation
st.markdown("""
    <style>
    /* Tab container */
    div[data-testid="stTabs"] button {
        transition: all 0.3s ease;
        border-radius: 8px;
        padding: 8px 16px;
        margin: 4px;
    }

    /* Hover effect */
    div[data-testid="stTabs"] button:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        transform: scale(1.05);
        background-color: #f0f0f0;
    }

    /* Active tab effect */
    div[data-testid="stTabs"] button[aria-selected="true"] {
        box-shadow: 0 6px 16px rgba(0,0,0,0.3);
        transform: scale(1.08);
        background-color: #ffe680;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)
# =========================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    '📊 About Dataset',
    '📈 Dashboard',
    '🤖 Machine Learning',
    '🔮 Prediction App',
    '📩 Contact Me'
])

# =========================
# TAB CONTENT
# =========================
with tab1:
    about_dataset.about_dataset()

with tab2:
    Vizz.chart()

with tab3:
    st.subheader("1. Preprocessing data")
    machine_learning.ml_model()

with tab4:
    Prediction_App.prediction_app()

with tab5:

    st.set_page_config(page_title="Taxi Trip Price Analysis & Prediction", layout="centered")

    # CSS untuk efek timbul saat hover
    card_style = """
    <style>
    .profile-card {
        background-color: #000000;
        color: #FFD700;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #FFD700;
        text-align: center;
        width: 320px;
        margin: auto;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .profile-card:hover {
        transform: scale(1.05);
        box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
    }
    .profile-card h4 {
        margin-bottom: 10px;
    }
    </style>
    """

    # HTML kartu profil
    card_html = """
    <div class="profile-card">
        <h4>Contact Me</h4>
        <p><b>Albertus Raditya Bagas Primaradi</b></p>
        <p>📧 itsbagasprimaradi@gmail.com</p>
        <p>💼 linkedin.com/in/bagasprimaradi</p>
        <p>📱 +62 896 5867 0069</p>
    </div>
    """
    st.markdown(card_style + card_html, unsafe_allow_html=True)

    # st.markdown("""
    # <div style="background-color:#000000;padding:20px;border-radius:10px;color:white">
    #     <h3>📩 Contact Me</h3>
    #     <p><strong>Albertus Raditya Bagas Primaradi</strong></p>
    #     <p>📧 Email: itsbagasprimaradi@gmail.com</p>
    #     <p>💼 LinkedIn: <a href='https://linkedin.com/in/bagasprimaradi' style='color:#FFB400'>linkedin.com/in/bagasprimaradi</a></p>
    #     <p>📱 +62 896 5867 0069</p>
    # </div>
    # """, 
    # unsafe_allow_html=True)


# =========================
# FOOTER
# =========================
st.divider()
st.markdown(
    "<p style='text-align:center; color:gray;'>© 2026 | Data Science Final Project</p>",
    unsafe_allow_html=True
)












 