import streamlit as st
import pandas as pd

st.title('Titanic')
st.header('Data set')
st.markdown('*priscila cervantes*')

df=pd.read_csv('Titanic-Dataset.csv')
st.dataframe(df)

 
