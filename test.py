import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

st.multiselect("Failure Modes", ["False obervation", "failing to observe"])
st.file_uploader("Image", "accept_multiple_files=False")

st.image(image)
