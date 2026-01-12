import streamlit as st
import pandas as pd
import plotly as px
import plotly.express as px


# Load dataset
def chart():
# =======================
# Page Config
# =======================
    st.set_page_config(
        page_title="Taxi Trip Dashboard",
        layout="wide"
    )

    # =======================
    # Custom CSS
    # =======================
    st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(180deg, #FFD76A, #FFCB45);
    }

    /* Header Card */
    .header-box {
        background: #000;
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.25);
    }

    /* Metric Card */
    .metric-card {
        background: rgba(255,255,255,0.85);
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0px 6px 16px rgba(0,0,0,0.15);
        transition: transform 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-5px);
    }

    /* Metric Number */
    .metric-value {
        font-size: 38px;
        font-weight: bold;
        color: #111;
    }

    /* Metric Label */
    .metric-label {
        font-size: 16px;
        color: #555;
    }

    /* Section Title */
    .section-title {
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 10px;
    }

    /* Button Style */
    .stButton>button {
        border-radius: 12px;
        padding: 8px 20px;
        border: none;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

    st.set_page_config(page_title="Dashboard Hover", layout="centered")

    # Tambahkan CSS untuk efek hover
    st.markdown("""
    <style>
    .header-box {
        background-color: #000000;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .header-box:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 25px rgba(0,0,0,0.4);
    }
    .header-box h1 {
        color: white;
        margin: 0;
        font-size: 32px;
    }
    </style>

    <div class="header-box">
        <h1>🚕 Dashboard Taxi Trip Price Analysis</h1>
    </div>
    """, unsafe_allow_html=True)


    st.write("")  # spacing

    # =======================
    # Load Data
    # =======================
    df = pd.read_csv("dataset.csv")

    # =======================
    # Session State
    # =======================
    if "selected_weather" not in st.session_state:
        st.session_state.selected_weather = None
    if "selected_traffic" not in st.session_state:
        st.session_state.selected_traffic = None

    # =======================
    # Metrics Section
    # =======================
    col1, col2, col3 = st.columns([2,2,2])

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Pelanggan</div>
            <div class="metric-value">{int(df['Passenger_Count'].sum())}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Jarak Rata-rata (km)</div>
            <div class="metric-value">{df['Trip_Distance_km'].mean():.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Durasi Rata-rata (menit)</div>
            <div class="metric-value">{df['Trip_Duration_Minutes'].mean():.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    # =======================
    # Filter Section
    # =======================
    st.write("")
    colA, colB, colC = st.columns([3,3,2])
    with colA:
        st.markdown("<div class='section-title'>🌦️ Kondisi Cuaca</div>", unsafe_allow_html=True)

        if st.button("Clear"):
            st.session_state.selected_weather = "Clear"
        if st.button("Rainy"):
            st.session_state.selected_weather = "Rainy"
        if st.button("Snowy"):
            st.session_state.selected_weather = "Snowy"

        # ✅ tampilkan selection
        if st.session_state.selected_weather:
            st.markdown(
                f"**Selected:** `{st.session_state.selected_weather}`"
            )
        else:
            st.markdown("_No weather selected_")

    # =======================
    # TRAFFIC FILTER
    # =======================
    with colB:
        st.markdown("<div class='section-title'>🚦 Kondisi Lalu Lintas</div>", unsafe_allow_html=True)

        if st.button("Low"):
            st.session_state.selected_traffic = "Low"
        if st.button("Medium"):
            st.session_state.selected_traffic = "Medium"
        if st.button("High"):
            st.session_state.selected_traffic = "High"

        # ✅ tampilkan selection
        if st.session_state.selected_traffic:
            st.markdown(
                f"**Selected:** `{st.session_state.selected_traffic}`"
            )
        else:
            st.markdown("_No traffic selected_")

    # =======================
    # RESET
    # =======================
    with colC:
        st.write("")
        st.write("")
        if st.button("🔄 Reset Filter"):
            st.session_state.selected_weather = None
            st.session_state.selected_traffic = None

    st.write("Dataset Preview:")
    st.dataframe(df.head())

    df=df.dropna()
    df_clean = df.dropna(subset=["Trip_Price", "Traffic_Conditions", "Weather", "Trip_Distance_km"])

    st.write("Cleaned Dataset Preview:")
    st.dataframe(df_clean)

    #Pie Chart
    
    # Hitung jumlah masing-masing kategori 
    category_df = df['Traffic_Conditions'].value_counts(dropna=False).reset_index()
    category_df.columns = ['Traffic_Conditions', 'count'] 
    # Buat figure dan pie chart Persentase Kondisi Lalu Lintas
    fig1 = px.pie(category_df, values='count', names='Traffic_Conditions',
            color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig1)
    st.markdown("""
    <div style='background-color:#f9f9f9; padding:20px; border-radius:10px; border-left:5px solid #FF9800'>
    <h4>🔍 Visualisasi Pie Chart Kondisi Lalu Lintas</h4>
    <ul>
    <li><b>📊 Insight dari Visualisasi:</b></li>
    <ul>
    <li>Sebagian besar perjalanan taksi berlangsung dalam kondisi lalu lintas <b>sedang</b>, mencerminkan pola mobilitas urban yang aktif namun belum mencapai titik kemacetan ekstrem.</li>
    <li>Proporsi perjalanan saat lalu lintas <b>lancar</b> hampir menyamai kondisi sedang, menandakan adanya waktu-waktu atau area yang masih efisien untuk transportasi.</li>
    <li>Kondisi lalu lintas <b>padat</b> hanya mencakup sekitar seperlima dari total perjalanan, namun tetap menjadi perhatian penting dalam perencanaan rute dan estimasi waktu tempuh.</li>
    </ul>
    <li><b>✅ Rekomendasi Strategis:</b></li>
    <ul>
    <li>Optimalkan rute pada kondisi lalu lintas lancar dan sedang untuk meningkatkan efisiensi operasional.</li>
    <li>Identifikasi area atau waktu dengan lalu lintas padat untuk perencanaan rute alternatif dan estimasi waktu yang lebih akurat.</li>
    <li>Gunakan informasi distribusi kondisi lalu lintas ini sebagai dasar pengembangan fitur prediksi waktu tempuh atau penetapan tarif dinamis.</li>
    <li>Komunikasikan kepada pelanggan bahwa sebagian besar perjalanan berlangsung dalam kondisi yang relatif efisien, sebagai nilai tambah layanan.</li>
    </ul>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    # Histogram Trip_Price
    fig2 = px.histogram(df_clean, x="Trip_Price", nbins=30,  
                            color_discrete_sequence=['skyblue'])
    st.plotly_chart(fig2)   
    st.markdown("""
    <div style='background-color:#f9f9f9; padding:20px; border-radius:10px; border-left:5px solid #FF9800'>
    <h4>🔍 Visualisasi Histogram Harga Perjalanan</h4>
    <ul>
    <li><b>📊 Insight dari Visualisasi:</b></li>
    <ul>
    <li>Histogram ini mengungkapkan distribusi harga perjalanan taksi, menunjukkan bahwa sebagian besar Distribusi harga perjalanan cenderung skewed ke kanan (lebih banyak perjalanan dengan harga rendah–menengah, tapi ada beberapa perjalanan dengan harga sangat tinggi/outlier).</li>
    </ul>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    # 2. Boxplot Trip_Price vs Traffic_Conditions
    fig3 = px.box(df_clean, x="Traffic_Conditions", y="Trip_Price", color="Traffic_Conditions",
                      title="Boxplot Harga Perjalanan berdasarkan Kondisi Lalu Lintas",
                      color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig3)
    st.markdown("""
    <div style='background-color:#f9f9f9; padding:20px; border-radius:10px; border-left:5px solid #FF9800'>
    <h4>🔍 Visualisasi Boxplot Harga Perjalanan berdasarkan Kondisi Lalu Lintas</h4>
    <ul>
    <li><b>📊 Insight dari Visualisasi:</b></li>
    <ul>
    <li>Insight: Kondisi lalu lintas tinggi (High) biasanya menghasilkan harga lebih tinggi dibanding kondisi rendah (Low). Hal ini masuk akal karena macet → durasi perjalanan lebih lama → biaya per menit bertambah. Outlier terlihat jelas pada kondisi tertentu, menandakan ada perjalanan yang jauh lebih mahal dari rata-rata.</li>
    </ul>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    # 4. Scatter plot Trip_Distance_km vs Trip_Price
    fig4 = px.scatter(df_clean, x="Trip_Distance_km", y="Trip_Price", opacity=0.6)
    fig4.update_layout(title="Hubungan Jarak dan Harga Perjalanan")
    st.plotly_chart(fig4)
    st.markdown("""
    <div style='background-color:#f9f9f9; padding:20px; border-radius:10px; border-left:5px solid #FF9800'>
    <h4>🔍 Visualisasi Scatter Plot Jarak vs Harga Perjalanan</h4>
    <ul>
    <li><b>📊 Insight dari Visualisasi:</b></li>
    <ul>
    <li>Insight: Cuaca hujan/salju cenderung menaikkan rata-rata harga perjalanan dibanding cuaca cerah. Kemungkinan karena durasi perjalanan lebih lama (jalan licin, macet) atau tarif tambahan saat cuaca buruk. Ini menunjukkan cuaca sebagai faktor penting dalam prediksi harga.</li>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

    # 5. Heatmap Korelasi dengan Trip_Price
        # Cara 1
    df_numerical = df_clean.select_dtypes(include='number').columns
    corr = df_clean[df_numerical].corr()
    fig5 = px.imshow(corr, color_continuous_scale="Blues", text_auto=".2f")
    st.plotly_chart(fig5)
    st.markdown("""
    <div style='background-color:#f9f9f9; padding:20px; border-radius:10px; border-left:5px solid #FF9800'>
    <h4>🔍 Visualisasi Heatmap Korelasi Variabel Numerik</h4>
    <ul>
    <li><b>📊 Insight dari Visualisasi:</b></li>
    <ul>
    <li>Insight: Ada hubungan positif antara jarak dan harga (semakin jauh → semakin mahal). Namun, hubungan tidak selalu linear sempurna: beberapa perjalanan dengan jarak pendek bisa mahal (mungkin karena durasi lama/traffic). Outlier terlihat jelas (jarak >100 km dengan harga >200), yang bisa memengaruhi model regresi jika tidak ditangani.</li>
    </div>
    """, unsafe_allow_html=True)
    
    # =========================
    # FEATURE ENGINEERING & VISUALIZATION
    df_visual = pd.read_csv("dataset.csv")
    df = df.copy()
    df["Cost_per_km"] = df["Trip_Price"] / df["Trip_Distance_km"]
    df["Cost_per_minute"] = df["Trip_Price"] / df["Trip_Duration_Minutes"]
    df["Is_Weekend"] = df["Day_of_Week"].isin(["Saturday", "Sunday"]).astype(int)
    df["Is_Peak_Hour"] = ((df["Time_of_Day"].isin(["Morning","Evening"])) & 
                            (df["Day_of_Week"]=="Weekday")).astype(int) 

    # Streamlit UI
    st.title("🚖 Data exploratiory with featured engineering")

    st.subheader("Preview Data")
    st.dataframe(df.head())

    # Histogram Cost per km
    fig10 = px.histogram(df, x="Cost_per_km", nbins=30, title="Distribusi Cost per km", color_discrete_sequence=["skyblue"])
    st.plotly_chart(fig10)
    st.markdown("""
        <div style='background-color:#f9f9f9; padding:20px; border-radius:10px; border-left:5px solid #4CAF50'>
        <li>🔍 Histogram Cost per km</li>
        <ul>
        <li><b>📊 Insight dari Visualisasi:</li>
        <ul>
        <li>Terdapat sedikit data dengan 'cost per km' di atas 10, yang bisa jadi merupakan outlier atau kasus khusus (misalnya perjalanan sangat pendek dengan tarif minimum, atau rute mahal).</li>
        <li>Lebih dari 80% data terkonsentrasi dengan cost dibawah 5/km, menandakan efisiensi biaya yang baik secara umum.</li>
        </ul>
        <li><b>✅ Rekomendasi Strategis</li>
        <ul>
        <li>Evaluasi rute dengan cost/km tinggi untuk kemungkinan penggabungan, promosi, atau penyesuaian armada.</li>
        <li>Gunakan distribusi ini sebagai dasar untuk menerapkan 'dynamic pricing'—misalnya, tarif lebih fleksibel untuk rute dengan permintaan tinggi namun biaya rendah.</li>
        </ul>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    st.write("")    

    # Histogram Cost per minute
    fig12 = px.histogram(df, x="Cost_per_minute", nbins=30, title="Distribusi Cost per minute", color_discrete_sequence=["orange"])
    st.plotly_chart(fig12)
    st.markdown("""
        <div style='background-color:#f9f9f9; padding:20px; border-radius:10px; border-left:5px solid #FF9800'>
        <h4>🔍 Histogram Cost per minute</h4>
        <ul>
        <li><b>📊 Insight dari Visualisasi:</li>
        <ul>
        <li>Mayoritas data memiliki 'cost per minute' di bawah 2, menunjukkan efisiensi biaya waktu yang baik.</li>
        <li>Ada beberapa data dengan cost per minute di atas 5, yang bisa jadi outlier atau kasus khusus (misalnya perjalanan singkat dengan tarif minimum atau kondisi lalu lintas ekstrem).</li>
        </ul>
        <li><b>✅ Rekomendasi Strategis</li>
        <ul>
        <li>Fokus pada rute dengan cost/minute rendah untuk meningkatkan efisiensi operasional.</li>
        <li>Evaluasi rute dengan cost/minute tinggi untuk kemungkinan penggabungan, promosi, atau penyesuaian armada.</li>
        <li>Gunakan distribusi ini sebagai dasar untuk menerapkan 'dynamic pricing'—misalnya, tarif lebih fleksibel untuk rute dengan permintaan tinggi namun biaya waktu rendah.</li>
        <li>Soroti bahwa mayoritas perjalanan memiliki cost/minute rendah sebagai nilai jual (value proposition) dalam kampanye pemasaran.</li>
        </ul>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    st.write("")

    # Boxplot Peak Hour vs Cost per minute
    fig14 = px.box(df, x="Is_Peak_Hour", y="Cost_per_minute", 
                    labels={"Is_Peak_Hour":"Peak Hour (1) vs Non-Peak (0)", "Cost_per_minute":"Cost per minute"},
                    color="Is_Peak_Hour")
    st.plotly_chart(fig14)
    st.markdown("""
    <div style='background-color:#f9f9f9; padding:20px; border-radius:10px; border-left:5px solid #FF9800'>
    <h4>🔍 Visualisasi Boxplot Cost per minute berdasarkan Peak Hour vs Non-Peak</h4>
    <ul>
    <li><b>📊 Insight dari Visualisasi:</b></li>
    <ul>
    <li>Biaya per menit cenderung lebih tinggi selama jam sibuk (Peak Hour) dibandingkan Non-Peak Hour.</li>
    <li>Distribusi selama Non-Peak Hour lebih lebar, menunjukkan variasi harga yang lebih besar dan banyak outlier di atas 10 cost/minute.</li>
    <li>Median biaya per menit selama Peak Hour justru lebih rendah, menandakan bahwa meskipun sibuk, tarif per menit bisa lebih stabil.</li>
    <li>Outlier selama Non-Peak Hour menunjukkan adanya perjalanan mahal yang tidak biasa, kemungkinan karena durasi lama atau kondisi khusus.</li>
    </ul>
    </ul>
    </div>
    """, unsafe_allow_html=True)



#==========================
