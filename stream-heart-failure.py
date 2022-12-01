import pickle
import streamlit as st

Heart_model = pickle.load(open('Heart_failure_model.sav', 'rb'))

st.title('Data Prediksi Gagal Ginjal')

Age = st.text_input('Input Nilai Age')

Sex = st.text_input('Input Nilai Sex')

ChestPainType = st.text_input('Input Nilai ChestPainType')

RestingBP = st.text_input('Input Nilai RestingBP')

Cholesterol = st.text_input('Input Nilai Cholesterol')

FastingBS = st.text_input('Input Nilai FastingBS')

RestingECG = st.text_input('Input Nilai RestingECG')

MaxHR = st.text_input('Input Nilai MaxHR')

ExerciseAngina = st.text_input('Input Nilai ExerciseAngina')

Oldpeak = st.text_input('Input Nilai Oldpeak')

ST_Slope = st.text_input('Input Nilai ST_Slope')

heart_diagnosis = ''

if st.button('Test Presiksi Gagal Jantung'):
    heart_diagnosis = Heart_model.predict([[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]])

    if(heart_diagnosis[0] == 1):
        heart_diagnosis = 'Pasien Terkena GAGAL GINJAL'
    else :
            heart_diagnosis = 'Pasien TIDAK Terkena GAGAL GINJAL'

    st.success(heart_diagnosis)
