import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file_path):
    data = pd.read_parquet(file_path, engine='fastparquet')
    
    # Ensuring column names are consistent and lowercase
    data.columns = [col.lower() for col in data.columns]
    
    if 'latitude' in data.columns and 'longitude' in data.columns:
        data['latitude'] = data['latitude'].fillna(method='ffill').fillna(method='bfill')
        data['longitude'] = data['longitude'].fillna(method='ffill').fillna(method='bfill')
    
    return data
