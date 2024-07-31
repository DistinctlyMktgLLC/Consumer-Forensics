import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file_path):
    data = pd.read_parquet(file_path, engine='fastparquet')
    
    if 'Latitude' in data.columns and 'Longitude' in data.columns:
        data['Latitude'] = data['Latitude'].fillna(method='ffill').fillna(method='bfill')
        data['Longitude'] = data['Longitude'].fillna(method='ffill').fillna(method='bfill')
    elif 'latitude' in data.columns and 'longitude' in data.columns:
        data['latitude'] = data['latitude'].fillna(method='ffill').fillna(method='bfill')
        data['longitude'] = data['longitude'].fillna(method='ffill').fillna(method='bfill')
    
    return data

