# -*- coding: utf-8 -*-
"""
Created on 30.11.2023

@author: DE-131847
"""

#Import the required Libraries
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

# Add a title and intro text
st.title('Geospatial Portfolio Analysis')
st.text('* * * * THIS APP IS A TEST * * * +')


with st.sidebar:
    st.title('Portfolio Upload:')
    with st.form(key='portfolio_upload'):
        upload_file = st.file_uploader('Upload a csv file with columns "id", "latitude", "longitude", "country", "value"')
        submitted = st.form_submit_button(label='Upload')


if submitted:
    if upload_file.name.endswith('.csv'):
        df = pd.read_csv(upload_file)
    else:
        st.sidebar.error('Please upload a csv or an Excel file', icon="🚨")
        st.stop()
    st.success(f'File {upload_file.name} successfully uploaded!', icon="✅")
        
    df['value'] = np.round(df['value'], 0)

    
if submitted or "expo" in st.session_state.keys():
    if "expo" in st.session_state.keys():
        df = st.session_state['expo']
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.map(df)

    with col2:   
        df_lvl0_hist = df.groupby(['country'], as_index=False)['value'].sum()
        
        st.text('Exposure distribution by country')
        st.bar_chart(df_lvl0_hist, x='country', y='value')

        
    st.write('The provided portfolio contains', len(df), 
             ' entries for a total exposure value of ', f'{np.round(df.value.sum(), 0):,}')
    
    st.dataframe(df.sort_values('value', ascending=False), hide_index=True)
    
    st.session_state['expo'] = df
    