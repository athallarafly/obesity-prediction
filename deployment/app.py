import streamlit as st
import eda
import prediction


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploratory Data Analysis (EDA)', 'Model Predictions'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Milestone 2')
    st.write('Nama      : Athalla Rafly Mahardhika Noegroho')
    st.write('Batch     : HCK - 009')
    st.write('Objective : ')
    st.write(
        f"""
        <div style="text-align: justify;">
        Membuat sebuah model Classification yang dapat melakukan prediksi untuk mengetahui Tipe Berat badan, apakah seseorang tersebut insufficient_weight, normal, Obesity_Type_I, Obesity_Type_II, Obesity_Type_III, Overweight_Level_I atau Overweight_Level_II </div>""", unsafe_allow_html=True)
    st.write(
        f"""
        <br></br>""", unsafe_allow_html=True)
    
    st.write('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
            st.caption(
            f"""
            <div style="font-size: 21.5px; text-align: justify;">
            Seiring berjalannya waktu, gaya hidup modern telah memengaruhi pola makan dan aktivitas fisik di seluruh dunia, yang telah berkontribusi pada peningkatan masalah obesitas.
            
            Data mencakup informasi tentang kebiasaan makan, kondisi fisik, usia, jenis kelamin, dan karakteristik individu lainnya.
            
            Data yang dikumpulkan kemudian diolah dan diberi label untuk menciptakan variabel kelas NObesity, yang mencerminkan tingkat obesitas individu. Ini dilakukan dengan merujuk pada panduan dari Organisasi Kesehatan Dunia (WHO). Hasil dari penelitian ini akan memberikan wawasan berharga tentang faktor-faktor yang mempengaruhi obesitas dan dapat membantu dalam pengembangan program-program pencegahan dan pengelolaan obesitas.
            </div>
            """,
            unsafe_allow_html=True)

    with st.expander("Problem Statement"):
            st.caption(
            f"""
            <div style="font-size: 21.5px; text-align: justify;">
            Peningkatan obesitas sebagai dampak dari perubahan gaya hidup modern memerlukan pemahaman mendalam tentang faktor-faktor yang mempengaruhi tingkat obesitas. Penelitian ini bertujuan untuk menganalisis data yang mencakup informasi tentang kebiasaan makan, kondisi fisik, dan karakteristik individu untuk memberikan wawasan yang berharga dan mendukung pengembangan program-program pencegahan dan manajemen obesitas yang lebih efektif.
            </div>
            """,
            unsafe_allow_html=True)
    with st.expander("Kesimpulan"):
        st.caption(
        f"""
        <div style="font-size: 21.5px; text-align: justify;">
        <ol> 
            <li>Dari Model yang sudah dibuat, Model sudah cukup baik dimana accuracy scorenya sudah cukup tinggi dan bagus. Data termasuk data yang bagus, karena tidak ada missing values.</li>
            <li>Langkah awal sebelum melakukan prediksi adalah dengan melihat pola hidup dan perilaku dari seseorang tersebut sebagai langkah awalnya. Dapat disimpulkan bahwa Rata - rata seseorang mulai termasuk obesitas jika melakukan pola hidup tidak sehat seperti jarang beraktivitas, konsumsi makanan berkalori tinggi, makan dengan porsi besar dan sering dalam sehari, kurang minum air putih, sering konsumsi gula dengan kadar tinggi seperti pada alkohol dan faktor pendukung lainnya jika memiliki riwayat keturunan obesitas juga.</li>
        </ol>
        </div>
        """,
        unsafe_allow_html=True)
elif page == 'Exploratory Data Analysis (EDA)':
    eda.run()
else:
     prediction.run()