import joblib
import streamlit as st
import pandas as pd
import plotly.express as px
import math
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score
from imblearn.over_sampling import SMOTE 
from sklearn.metrics import ConfusionMatrixDisplay

def ml_model():
    df = pd.read_csv("dataset.csv")
    df = df.dropna()
    
    # Preprocessing
    numerical = df.select_dtypes(include=['number']).columns

    df = df[numerical].copy()

    X = df.drop('Trip_Price', axis=1)  
    Y = df['Trip_Price']

    #cek outlier
    Q1 = df[numerical].quantile(0.25)
    Q3 = df[numerical].quantile(0.75)     
    IQR = Q3 - Q1
    #menentukan batas bawah dan batas atas
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    st.write(f"Jumlah data sebelum pembersihan: **{df.shape[0]} baris**")

    #menghapus outlier
    df = df[~((df[numerical] < lower_bound) | (df[numerical] > upper_bound)).any(axis=1)]
    st.write(f"Jumlah data setelah pembersihan outlier: **{df.shape[0]} baris**")

    #Feature Encoding
    df_select = pd.get_dummies(df, drop_first=True)

    #6. Normalisasi kolom numerik dengan MinMax Scaler
    st.write('### 2. Normalisasi menggunakan MinMax Scaler')
    for col in numerical:
        df_select[col] = MinMaxScaler().fit_transform(df_select[col].values.reshape(len(df_select), 1))
        st.write(f'Normalisasi kolom {col} selesai.')
    st.dataframe(df_select.head())

    st.write('### 3. Korelasi Linear antar Kolom Numerik')
    #7.a Correlation Heatmap
    st.write('**Correlation Heatmap**')
    corr = df_select[numerical].corr().round(2)
    fig = px.imshow(corr, text_auto=True, aspect="auto", title='Correlation Heatmap')
    st.plotly_chart(fig, use_container_width=True)

    st.write('Heatmap ini menunjukkan hubungan antar fitur numerik dalam dataset, dengan nilai ' \
            'korelasi berkisar dari -1 (berlawanan sempurna) hingga +1 (sejalan sempurna). ' \
            'Semakin mendekati 0, semakin lemah hubungannya')
    
    #8. Mengecek nilai VIF setiap kolom
    from statsmodels.stats.outliers_influence import variance_inflation_factor

    vif_data = pd.DataFrame()
    vif_data["feature"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) 
                    for i in range(X.shape[1])]
    vif_data
    st.write('### 4. Variance Inflation Factor (VIF) untuk Mendeteksi Multikolinearitas')
    st.dataframe(vif_data)

    X = df_select.drop('Trip_Price', axis=1)  
    Y = df_select['Trip_Price']

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    st.write('#### Data Latih dan Data Uji')
    st.dataframe(X_train.head())
    st.write(f'Jumlah data latih: {X_train.shape[0]} baris')
    st.dataframe(X_test.head())
    st.write(f'Jumlah data uji: {X_test.shape[0]} baris')

    #9. Normalisasi Data
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    st.write('### 5. Pembuatan Model Machine Learning - Regresi Linear')
    from sklearn.linear_model import LinearRegression

    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    #modeling dgn regresi liner
    # Melihat koefisien masing-masing fitur
    coef_df = pd.DataFrame({
        'feature': X.columns,
        'coefficient': model.coef_
    })
    # Melihat nilai intercept
    st.write("Intercept:", model.intercept_)

    st.dataframe(coef_df)


    st.write('### 6. Tuning Hyperparameter pada Model Ridge Regression')
    from sklearn.model_selection import GridSearchCV
    from sklearn.linear_model import Ridge
    import numpy as np

    #Pada Ridge
    ridge = Ridge()
    alphas = np.logspace(-3, 3, 20)  # λ dari 0.001 sampai 1000
    param_grid = {'alpha': alphas}
    grid = GridSearchCV(ridge, param_grid, cv=10, scoring='neg_mean_squared_error')
    grid.fit(X_train_scaled, y_train)

    st.write("Best alpha:", grid.best_params_)
    st.write("Best score:", grid.best_score_)

    st.write('### 7. Tuning Hyperparameter pada Model Lasso Regression')
    #Pada Lasso
    from sklearn.linear_model import Lasso
    lasso = Lasso()
    alphas = np.logspace(-3, 3, 20)  # λ dari 0.001 sampai 1000
    param_grid = {'alpha': alphas}
    grid = GridSearchCV(lasso, param_grid, cv=5, scoring='neg_mean_squared_error')
    grid.fit(X_train_scaled, y_train)
    
    st.write("Best alpha:", grid.best_params_)
    st.write("Best score:", grid.best_score_)

    st.write('### 8. Modeling menggunakan Ridge Regression dengan alpha terbaik')
    from sklearn.linear_model import Ridge
    ridge = Ridge(alpha=0.001)
    ridge.fit(X_train_scaled, y_train)
    # Melihat koefisien masing-masing fitur
    coef_df_ridge = pd.DataFrame({
        'feature': X.columns,
        'coefficient': ridge.coef_
    })
    coef_df_ridge
    st.dataframe(coef_df_ridge)

    st.write('### 9. Modeling menggunakan Lasso Regression dengan alpha terbaik')
    from sklearn.linear_model import Lasso
    lasso = Lasso(alpha=0.078)
    lasso.fit(X_train_scaled, y_train)
    # Melihat koefisien masing-masing fitur
    coef_df_lasso = pd.DataFrame({
        'feature': X.columns,
        'coefficient': lasso.coef_
    })
    coef_df_lasso
    st.dataframe(coef_df_lasso)

    st.write('### 10. Evaluasi Model')
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score 
    import numpy as np

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Evaluasi Model Linear Regression")
        # Prediksi
        y_pred = model.predict(X_test)
        # MAE
        mae = mean_absolute_error(y_test, y_pred)
        # MAPE (gunakan rumus manual karena sklearn tidak menyediakan)
        mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
        # RMSE
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        # R2 Score
        r2 = r2_score(y_test, y_pred)

        st.write("MAE :", mae)
        st.write("MAPE:", mape, "%")
        st.write("RMSE:", rmse)
        st.write("R2:", r2)

    with col2:
        st.header("Evaluasi Model Ridge Regression")
        # Prediksi
        y_pred = ridge.predict(X_test_scaled)
        # MAE
        mae_ridge = mean_absolute_error(y_test, y_pred)
        # MAPE (gunakan rumus manual karena sklearn tidak menyediakan)
        mape_ridge = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
        # RMSE
        rmse_ridge = np.sqrt(mean_squared_error(y_test, y_pred))
        # R2 Score
        r2_ridge = ridge.score(X_test_scaled, y_test)

        st.write("MAE :", mae_ridge)
        st.write("MAPE:", mape_ridge, "%")
        st.write("RMSE:", rmse_ridge)
        st.write("R2:", r2_ridge)

    # st.write('Evaluasi model ridge regression:')
    # # Prediksi
    # y_pred = ridge.predict(X_test_scaled)
    # # MAE
    # mae_ridge = mean_absolute_error(y_test, y_pred)
    # # MAPE (gunakan rumus manual karena sklearn tidak menyediakan)
    # mape_ridge = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
    # # RMSE
    # rmse_ridge = np.sqrt(mean_squared_error(y_test, y_pred))
    # # R2 Score
    # r2_ridge = ridge.score(X_test_scaled, y_test)

    # st.write("MAE :", mae_ridge)
    # st.write("MAPE:", mape_ridge, "%")
    # st.write("RMSE:", rmse_ridge)
    # st.write("R2:", r2_ridge)

    with col3:
        st.header("Evaluasi Model Lasso Regression")
        # Prediksi
        y_pred = lasso.predict(X_test_scaled)
        # MAE
        mae_lasso = mean_absolute_error(y_test, y_pred)
        # MAPE (gunakan rumus manual karena sklearn tidak menyediakan)
        mape_lasso = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
        # RMSE
        rmse_lasso = np.sqrt(mean_squared_error(y_test, y_pred))
        # R2 Score
        r2_lasso = lasso.score(X_test_scaled, y_test)

        st.write("MAE :", mae_lasso)
        st.write("MAPE:", mape_lasso, "%")
        st.write("RMSE:", rmse_lasso)
        st.write("R2:", r2_lasso)
    
    st.markdown("### 📌 Insight Utama & Rekomendasi")
    st.markdown("""
    <div style='background-color:#f9f9f9; padding:20px; border-radius:10px; border-left:5px solid #4CAF50'>
    <h4>🔍 Insight Utama</h4>
    <ul>
    <li><b>Ridge Regression</b> unggul secara konsisten di semua metrik:</li>
    <ul>
    <li>MAE dan RMSE paling rendah → prediksi paling akurat secara absolut dan kuadrat.</li>
    <li>MAPE paling kecil → kesalahan relatif terhadap nilai aktual juga paling kecil.</li>
    <li>R² sangat tinggi (0.9061) → model menjelaskan 90% variabilitas data, sangat baik.</li>
    </ul>
    <li><b>Linear Regression</b> performa terburuk:</li>
    <ul>
    <li>MAE dan RMSE paling tinggi → prediksi paling meleset.</li>
    <li>MAPE sangat besar (228%) → kesalahan relatif sangat tinggi.</li>
    <li>R² negatif → model lebih buruk daripada sekadar rata-rata, tidak layak digunakan.</li>
    </ul>
    <li><b>Lasso Regression</b> berada di tengah:</li>
    <ul>
    <li>Lebih baik dari Linear, tapi jauh tertinggal dari Ridge.</li>
    <li>R² positif tapi rendah (0.4451) → hanya menjelaskan 44% variabilitas data.</li>
    </ul>
    </ul>

    <h4>✅ Rekomendasi</h4>
    <ul>
    <li>Gunakan <b>Ridge Regression</b> untuk prediksi karena memberikan hasil paling stabil dan akurat.</li>
    <li>Hindari <b>Linear Regression</b> dalam kasus ini karena performanya sangat buruk.</li>
    <li><b>Lasso Regression</b> bisa dipertimbangkan jika ada kebutuhan untuk fitur seleksi (karena sifat regularisasi L1), tapi tetap kalah dari Ridge dalam akurasi.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)



    st.write('### 10. Prediction App menggunakan Ridge Regression:')
    joblib.dump(ridge, "ridge_regression_model.pkl")
    joblib.dump(X.columns, "numeric_columns.pkl")    

    coef_df_ridge = pd.DataFrame({
    'feature': X.columns,
    'coefficient': ridge.coef_
    })
    st.dataframe(coef_df_ridge)

