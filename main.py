import streamlit as st
import numpy as np

import datetime

import plotly.graph_objects as go

st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_title='Stock Forecast Streamlit')
st.title("Stock Forecast Dashboard")

window_selection_c = st.sidebar.container()
window_selection_c.markdown("## Insights")
sub_columns = window_selection_c.columns(2)