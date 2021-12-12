# ---------------------------------------- #
#                 IMPORTS                  #
# ---------------------------------------- #

# interface
import streamlit as st

# data manipulation
import pandas as pd

# data vis
import matplotlib.pyplot as plt
import plotly
import plotly.express as px

# project files
from charts import *

# load files
df = pd.read_pickle('data/df_happiness.pkl')

# ---------------------------------------- #
#              PAGE SETTINGS               #
# ---------------------------------------- #

title = 'World Happiness Report Data Vis'

st.set_page_config(
    page_title = title
)

# ---------------------------------------- #
#              PAGE ELEMENTS               #
# ---------------------------------------- #

st.title(title)

st.plotly_chart(scatter_chart(df))