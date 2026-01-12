import streamlit as st
import pandas as pd

def about_dataset():


    # st.markdown("### 📌 Informasi Dataset")
    # st.markdown("""
    # <div style='background-color:#f9f9f9; padding:20px; border-radius:10px; border-left:5px solid #4CAF50'>
    # col1, col2 = st.columns([5,5])

    # with col1:
    #     link = 'https://info.vd.ch/fileadmin/canton-communes/No_48/Reglement_sur_le_service_des_taxis.jpg'
    #     st.image(link, caption='gambar taxi')
    
    # with col2:
    #     st.write(' Dataset ini menunjukkan variasi harga yang dipengaruhi oleh kombinasi faktor jarak, ' \
    #             'durasi, kondisi lalu lintas, dan cuaca. Misalnya, perjalanan dengan jarak sangat panjang (lebih dari 100 km) ' \
    #             'menghasilkan harga di atas 200–300 satuan, sedangkan perjalanan pendek di bawah 5 km bisa menghasilkan harga belasan saja. ' \
    #             'Ada juga banyak nilai yang hilang (missing values) pada kolom Base_Fare, Per_Km_Rate, atau Trip_Price, yang menandakan data ini' \
    #             ' perlu pembersihan sebelum digunakan untuk analisis atau pemodelan.')
    
    # st.write('Pola menarik terlihat pada kondisi lalu lintas dan cuaca:tarif cenderung lebih tinggi saat hujan atau salju, serta ketika lalu lintas padat. ' \
    #         'Dengan struktur seperti ini, dataset cocok untuk eksplorasi regresi harga taksi, analisis faktor yang paling berpengaruh, maupun penerapan' \
    #         ' machine learning untuk prediksi harga perjalanan.')

    # st.write('**Variable dalam dataset:**')    
    # st.markdown(
    #     'Trip_Distance_km → Jarak perjalanan (dalam kilometer).  \n'
    #     'Time_of_Day → Waktu perjalanan (Pagi, Siang, Sore, Malam).  \n'
    #     'Day_of_Week → Hari kerja atau akhir pekan.  \n'
    #     'Passenger_Count → Jumlah penumpang.  \n'
    #     'Traffic_Conditions → Kondisi lalu lintas (Rendah, Sedang, Tinggi).  \n'
    #     'Weather → Cuaca (Cerah, Hujan, Salju).  \n'
    #     'Base_Fare → Tarif dasar (biaya awal).  \n'
    #     'Per_Km_Rate → Biaya per kilometer.  \n'
    #     'Per_Minute_Rate → Biaya per menit.  \n'
    #     'Trip_Duration_Minutes → Durasi perjalanan (menit).  \n'
    #     'Trip_Price → Harga akhir perjalanan (variabel target).'

    st.markdown("""
    <div style='background-color:#f9f9f9; padding:20px; border-radius:10px; border-left:5px solid #2196F3'>
    <h3>📊 Deskripsi Dataset</h3>
    <p>
    Dataset ini menunjukkan variasi harga yang dipengaruhi oleh kombinasi faktor jarak, durasi, kondisi lalu lintas, dan cuaca.
    Misalnya, perjalanan dengan jarak sangat panjang (lebih dari 100 km) menghasilkan harga di atas 200–300 satuan,
    sedangkan perjalanan pendek di bawah 5 km bisa menghasilkan harga belasan saja.
    Ada juga banyak nilai yang hilang (missing values) pada kolom <i>Base_Fare</i>, <i>Per_Km_Rate</i>, atau <i>Trip_Price</i>,
    yang menandakan data ini perlu pembersihan sebelum digunakan untuk analisis atau pemodelan.
    </p>

    <p>
    Pola menarik terlihat pada kondisi lalu lintas dan cuaca: tarif cenderung lebih tinggi saat hujan atau salju,
    serta ketika lalu lintas padat. Dengan struktur seperti ini, dataset cocok untuk eksplorasi regresi harga taksi,
    analisis faktor yang paling berpengaruh, maupun penerapan machine learning untuk prediksi harga perjalanan.
    </p>

    <h4>📌 Variabel dalam dataset:</h4>
    <ul>
    <li><b>Trip_Distance_km</b> → Jarak perjalanan (km)</li>
    <li><b>Time_of_Day</b> → Waktu perjalanan (Pagi, Siang, Sore, Malam)</li>
    <li><b>Day_of_Week</b> → Hari kerja atau akhir pekan</li>
    <li><b>Passenger_Count</b> → Jumlah penumpang</li>
    <li><b>Traffic_Conditions</b> → Kondisi lalu lintas (Rendah, Sedang, Tinggi)</li>
    <li><b>Weather</b> → Cuaca (Cerah, Hujan, Salju)</li>
    <li><b>Base_Fare</b> → Tarif dasar</li>
    <li><b>Per_Km_Rate</b> → Biaya per kilometer</li>
    <li><b>Per_Minute_Rate</b> → Biaya per menit</li>
    <li><b>Trip_Duration_Minutes</b> → Durasi perjalanan (menit)</li>
    <li><b>Trip_Price</b> → Harga akhir perjalanan (target)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
