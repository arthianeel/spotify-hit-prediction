import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title('Spotify Popularity Prediction')

# Danceability input
danceability = 0.000
danceability = st.slider("Enter Danceability", min_value=0.000, max_value=1.000, value=danceability, step=0.001)
# Energy input
energy = 0.000
energy = st.slider("Enter Energy", min_value=0.000, max_value=1.000, value=energy, step=0.001)
# Key input
key = 0
key = st.slider("Enter Key", min_value=0, max_value=11, value=key, step=1)
# Loudness input
loudness = st.number_input("Enter loudness (dB):", min_value=-1e308, max_value= 1.797e+308, value= 0.00)
# Mode input
mode = st.radio("Enter mode", (0,1))
# Speechiness input
speechiness = st.number_input("Enter speechiness (0-1):")
speechiness = f'{speechiness:.5f}'
# Acousticness input
acousticness = 0.000
acousticness = st.slider("Enter Acousticness", min_value=0.000, max_value=1.000, value=acousticness, step=0.001)
# Instrumentalness input
instrumentalness = 0.000
instrumentalness  = st.slider("Enter Instrumentalness", min_value=0.000, max_value=1.000, value=instrumentalness , step=0.001)
# Liveness input
Liveness = 0.000
Liveness = st.slider("Enter Liveness", min_value=0.000, max_value=1.000, value=Liveness, step=0.001)
# Valence input
valence = 0.000
valence = st.slider("Enter Valence", min_value=0.000, max_value=1.000, value=valence, step=0.001)
# Tempo input
tempo = st.number_input("Enter Chorus hit :")
# Duration input
duration_ms = st.number_input("Enter duration (ms):", step=1)
# Time signature input
time_signature = 0
time_signature = st.slider("Enter Time Signature", min_value=0, max_value=7, value=time_signature, step=1)
# Chorus hit input
chorus_hit = st.number_input("Enter Chorus hit (0 or 1):", step=0.001)
# Sections input
sections = st.number_input("Enter sections:")
# Decade input
decade = st.number_input("Enter decade (YYYY):", value=1969)
input = (danceability, energy, key,	loudness,mode,speechiness,acousticness,instrumentalness,Liveness,valence,tempo,duration_ms,time_signature,chorus_hit,sections,decade)
loaded_model = joblib.load('clf.pkl')
if st.button("Predict"):
   result = loaded_model.predict([input])
if result == 1:
    st.success("Hit")
else:
    st.error("Flop")