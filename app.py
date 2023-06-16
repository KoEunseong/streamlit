import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import folium

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.line_chart(df)
