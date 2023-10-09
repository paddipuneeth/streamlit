
import streamlit as st
import pandas as pd

#df = pd.read_csv(r"F:\A\DSML\Multivariate Analytics\Data")
df = pd.DataFrame()

st.set_page_config(
    page_title = "VX",
    layout = 'wide')

st.header("Hello SONY")
st.dataframe(df.head(10))