import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Exploratory Data Analysis (EDA)')
#Memanggil data csv 
    df= pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')

#menampilakn 5 data teratas
    st.table(df.head(5))

    st.title('Data Visualization')

# start 
    with st.expander('Melihat Distribusi Tipe Berat Badan'):
        st.write(
        f"""
        <div style="font-size: 28px; text-align: justify;">Melihat Distribusi Tipe Berat Badan</div>
        """,
        unsafe_allow_html=True,
    )
        image = Image.open('img/distribusiTipeBerat.jpg')
        st.image(image)

        st.caption(
        f"""
        <div style="font-size: 21.5px;">Insight : 
            <ul> 
            <li>Insufficient_Weight memiliki pesebaran paling sedikit</li>
            <li>Obesity_Type_I memiliki pesebaran paling banyak</li>
            </ul>
        Dari data ini dapat disimpulkan bahwa sudah banyak orang yang bertipe berat badan Obesitas dikarenakan pesebaran data Insufficient_weight (Berat badan kurang) dan Normal_Weight memiliki pesebaran yang paling sedikit dan sisanya sudah masuk tipe berat badan yang tidak baik atau obesitas.</div>
        """,
        unsafe_allow_html=True)

# end 

# start 
    with st.expander('Melihat di umur berapa yang paling banyak tipe berat badan Obesity_Type_III'):
        st.write(
        f"""
        <div style="font-size: 28px; text-align: justify;">Melihat di umur berapa yang paling banyak tipe berat badan Obesity_Type_III</div>
        """,
        unsafe_allow_html=True,
    )
        image = Image.open('img/output_eda2.png')
        st.image(image)
        st.caption(
        f"""
        <div style="font-size: 20px; text-align: justify;">Insight :

        Tipe Berat badan Obesity_Type_III paling banyak dialami oleh umur diatas 20 tahun, dapat disimpulkan bahwa pada range umur ini banyak orang yang melakukan pola hidup tidak sehat yang mengakibatkan obesitas </div>
        """,
        unsafe_allow_html=True)

# end 

# start
    with st.expander('Melihat rata - rata usia berdasarkan tipe berat badannya'):
        st.write(
        f"""
        <div style="font-size: 28px; text-align: justify;">Melihat rata - rata usia berdasarkan tipe berat badannya</div>
        """,
        unsafe_allow_html=True,
    )
        image = Image.open('img/output_eda3.png')
        st.image(image)
        st.caption(
        f"""
        <div style="font-size: 21.5px;">Insight : 
            <ul> 
            <li>Rata - rata dari tipe berat badan berada pada umur 20 tahun keatas</li>
            <li>Obesity_Type_II memiliki rata - rata usia paling tinggi</li>
            <li>Insufficient_Weight memiliki rata - rata usia paling rendah</li>
            </ul>
        Dari data ini dapat disimpulkan bahwa rata - rata orang mulai masuk ke tipe berat badan obesitas pada usia muda yang bisa disebabkan karena pola hidup tidak sehat.</div>
        """,
        unsafe_allow_html=True)

# end 

# start
    with st.expander('Melihat Distribusi Tipe berat badan berdasarkan Gender'):
        st.write(
        f"""
        <div style="font-size: 28px; text-align: justify;">Melihat Distribusi Tipe berat badan berdasarkan Gender</div>
        """,
        unsafe_allow_html=True,
    )
        image = Image.open('img/output_eda4.png')
        st.image(image)
        st.caption(
        f"""
        <div style="font-size: 21.5px;">Insight : 
            <ul> 
            <li>Perempuan memiliki jumlah terbanyak di Obesity_Type_III</li>
            <li>Laki - laki memiliki jumlah terbanyak di Obesity_Type_II</li>
            </ul>
        Berdasarkan data ini dapat dilihat bahwa Obesitas tidak mengenal gender, semua bisa terkena obesitas jika tidak melakukan pola hidup sehat.</div>
        """,
        unsafe_allow_html=True)

# end

# start
    with st.expander('Melihat Distribusi Tipe Berat Badan berdasarkan Umur'):
        st.write(
        f"""
        <div style="font-size: 28px; text-align: justify;">Melihat Distribusi Tipe Berat Badan berdasarkan Umur</div>
        """,
        unsafe_allow_html=True,
    )
        image = Image.open('img/output_eda5.png')
        st.image(image)
        st.caption(
        f"""
        <div style="font-size: 21.5px;">Insight : 
            <ul> 
            <li>Semua tipe berat badan berada di range umur 20 - 30 tahun</li>
            <li>Obesity_Type_I dan Overweight_Level_II memiliki data paling banyak</li>
            <li>Titik-titik yang jauh dari gugusan utama dapat dianggap sebagai outlier. Di "Normal_Weight,"dapat dilihat beberapa titik yang jauh lebih tinggi dari gugusan utama, menunjukkan beberapa individu yang lebih tua dalam kategori ini dibandingkan dengan mayoritas</li>
            </ul>
        Dari data tersebut dapat dilihat bahwa range umur pada distribusi ini terbanyak ada di range umur 20 - 30. Dari range umur tersebut dapat dilihat bahwa banyak yang sudah obesitas dan berat badan kurang.</div>
        """,
        unsafe_allow_html=True)

# end

# start
    with st.expander('Melihat persentasi banyaknya perokok yang mempunyai tipe berat badan Overweight_Level_II'):
        st.write(
        f"""
        <div style="font-size: 28px; text-align: justify;">Melihat persentasi banyaknya perokok yang mempunyai tipe berat badan Overweight_Level_II</div>
        """,
        unsafe_allow_html=True,
    )
        image = Image.open('img/output_eda6.png')
        st.image(image)
        st.caption(
        f"""
        <div style="font-size: 21.5px;">Insight : 
        Tipe berat badan Overweight_Level_II mayoritas bukan perokok, jadi merokok bukan salah satu faktor pasti untuk orang menjadi obesitas</div>
        """,
        unsafe_allow_html=True)

# end

# start
    with st.expander('Melihat apakah memiliki riwayat keturunan merupakan salah satu faktor terkena obesitas'):
        st.write(
        f"""
        <div style="font-size: 28px; text-align: justify;">Melihat apakah memiliki riwayat keturunan merupakan salah satu faktor terkena obesitas.</div>
        """,
        unsafe_allow_html=True,
    )
        image = Image.open('img/output_eda7.png')
        st.image(image)
        st.caption(
        f"""
        <div style="font-size: 21.5px;">Insight : 
        Dari data ini dapat disimpulkan bahwa jika memiliki riwayat obesitas merupakan salah satu faktor terbesar orang tersebut juga dapat obesitas</div>
        """,
        unsafe_allow_html=True)

# end

# start
    with st.expander('Apakah konsumsi kalori tinggi jadi faktor terkena obesitas'):
        st.write(
        f"""
        <div style="font-size: 28px; text-align: justify;">Apakah konsumsi kalori tinggi jadi faktor terkena obesitas.</div>
        """,
        unsafe_allow_html=True,
    )
        image = Image.open('img/output_eda8.png')
        st.image(image)
        st.caption(
        f"""
        <div style="font-size: 21.5px;">Insight : 
        Dari data ini dapat dilihat bahwa pengkonsumsi kalori tinggi terbanyak ada di Obesity_Type_I yang berarti adalah makanan dengan kalori tinggi merupakan salah satu faktor pendukung untuk seseorang dapat bertipe obesitas jika dibarengi dengan pola hidup tidak sehat.</div>
        """,
        unsafe_allow_html=True)

# end