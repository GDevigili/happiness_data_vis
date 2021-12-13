
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
from source.scatter_chart import *
from source.map import *
from source.utils import *


# ---------------------------------------- #
#             GLOBAL VARIABLES             #
# ---------------------------------------- #

# load files
df = pd.read_pickle('data/df_happiness.pkl')

# copy the df to another variable
df_aux = df

def change_df(df_changed):
    global df_aux
    df_aux = df_changed


# ---------------------------------------- #
#              PAGE SETTINGS               #
# ---------------------------------------- #

title = 'World Happiness Report Data Vis'

# Page settings
st.set_page_config(
    page_title = title,
    layout = 'wide'
)

# Add the title
st.title(title)


# ---------------------------------------- #
#                SIDE BAR                  #
# ---------------------------------------- #

# Title
st.sidebar.title('Filter the data:')

# Country multiselector
selected_countries = st.sidebar.multiselect(
    label = 'Countries:', 
    options = df.country.unique(), 
    default = ['Brazil', 'United States', 'United Kingdom', 
                'Italy', 'Germany', 'Argentina', 'Uruguay', 
                'Paraguay', 'Finland', 'Denmark', 'Switzerland',
                'Afghanistan', 'Zimbabwe', 'Rwanda']
)

change_df(df[df.country.isin(selected_countries)])

# Checkbox for sorting
sort = st.sidebar.checkbox(
    'Ascending order of happiness', 
    value = True)


# ---------------------------------------- #
#              PAGE ELEMENTS               #
# ---------------------------------------- #
 
scatter = render_scatter(df_aux, sort)

map_chart = render_map(df)