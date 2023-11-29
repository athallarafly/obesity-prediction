import streamlit as st
import pandas as pd
import pickle
from PIL import Image

def run():
# Load All Files

    with open('model_rf.pkl', 'rb') as file:
        full_process = pickle.load(file)

# Start Gender
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        Gender
        </div>
        """,
    unsafe_allow_html=True)
    Gender = st.selectbox(label='Choose your Gender here', options=['Female', 'Male'])
# End Gender

# Start Age
    Age = st.number_input(label='Input your Age Here', min_value=0)
# End Age

# Start Height
    Height = st.number_input(label='Input your Height Here', min_value=0)
# End Height

# Start Weight
    Weight = st.number_input(label='Input your Weight Here', min_value=0)
# End Weight

# Start fam
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        family_history_with_overweight
        </div>
        """,
    unsafe_allow_html=True)
    family_history_with_overweight = st.selectbox(label='Choose your family_history_with_overweight here', options=['yes', 'no'])
# End fam

# Start FAVC
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        FAVC
        </div>
        """,
    unsafe_allow_html=True)
    FAVC = st.selectbox(label='Choose your FAVC here', options=['yes', 'no'])
# End FAVC

# Start FCVC
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        FCVC
        </div>
        """,
    unsafe_allow_html=True)
    FCVC = st.selectbox(label='Choose your FCVC here', options=[1, 2, 3])
# End FCVC

# Start NCP
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        NCP
        </div>
        """,
    unsafe_allow_html=True)
    NCP = st.selectbox(label='Choose your NCP here', options=[1, 2, 3])
# End NCP

# Start CAEC
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        CAEC
        </div>
        """,
    unsafe_allow_html=True)
    CAEC = st.selectbox(label='Choose your CAEC here', options=['no', 'Sometimes', 'Frequently'])
# End CAEC

# Start SMOKE
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        SMOKE
        </div>
        """,
    unsafe_allow_html=True)
    SMOKE = st.selectbox(label='Choose your SMOKE here', options=['yes', 'no'])
# End SMOKE

# Start CH2O
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        CH2O
        </div>
        """,
    unsafe_allow_html=True)
    CH2O = st.selectbox(label='Choose your CH2O here', options=[1,2, 3])
# End CH2O

# Start SCC
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        SCC
        </div>
        """,
    unsafe_allow_html=True)
    SCC = st.selectbox(label='Choose your SCC here', options=['yes', 'no'])
# End SCC

# Start FAF
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        FAF
        </div>
        """,
    unsafe_allow_html=True)
    FAF = st.selectbox(label='Choose your FAF here', options=[1, 2, 3])
# End FAF

# Start TUE
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        TUE
        </div>
        """,
    unsafe_allow_html=True)
    TUE = st.selectbox(label='Choose your TUE here', options=[2, 3])
# End TUE

# Start CALC
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        CALC
        </div>
        """,
    unsafe_allow_html=True)
    CALC = st.selectbox(label='Choose your CALC here', options=['no', 'Sometimes', 'Frequently'])
# End CALC

# Start MTRANS
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        MTRANS
        </div>
        """,
    unsafe_allow_html=True)
    MTRANS = st.selectbox(label='Choose your MTRANS here', options=['Public_Transportation', 'Walking', 'Automobile', 'Motorbike', 'Bike'])
# End MTRANS

    st.write('In the following is the result of the data you have input : ')
    
    data_inf = pd.DataFrame({
        'Gender' : Gender,
        'Age' : Age,
        'Height' : Height,
        'Weight' : Weight,
        'family_history_with_overweight' : family_history_with_overweight,
        'FAVC' : FAVC,
        'FCVC' : FCVC,
        'NCP' : NCP,
        'CAEC' : CAEC,
        'SMOKE' : SMOKE,
        'CH2O' : CH2O,
        'SCC' : SCC,
        'FAF' : FAF,
        'TUE' : TUE,
        'CALC' : CALC,
        'MTRANS' : MTRANS,
        }, index=[0])

    st.table(data_inf)


    if st.button(label='Predict'):
    
        # Melakukan prediksi data
        y_pred_inf = full_process.predict(data_inf)

        
        st.metric(label="Here is a prediction of obes", value = y_pred_inf[0])
        st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        Default Payment Next Month
        <ol>
            <li>Insufficient Weight </li>   
            <li>Normal</li>
            <li>Obesity Type I</li> 
            <li>Obesity Type II</li>
            <li>Obesity Type III</li>
            <li>Overweight Level I</li>
            <li>Overweight Level II</li> 
        </ol>
        </div>
        """,
        unsafe_allow_html=True)

