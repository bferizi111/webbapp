# -*- coding: utf-8 -*-
"""
Created on 30.11.2023

@author: DE-131847
"""

#Import the required Libraries
import streamlit as st
import numpy as np
import pandas as pd

st.title('Customer Geolocalization')

expo = st.session_state['expo']
df = expo.copy()

with st.sidebar:
    customer_ids = st.multiselect('Select some client ID numbers',
                                   np.arange(df.id.min(), df.id.max()),
                                   [df.id.min()])

if customer_ids:
    st.write('Selected customers:')
    st.dataframe(df[df.id.isin(customer_ids)], hide_index=True)
    st.map(df[df.id.isin(customer_ids)])