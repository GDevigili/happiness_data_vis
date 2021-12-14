
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
from source.main_chart import *
from source.map import *
from source.line import *
from source.sccatter import *

from source.utils import *


# ---------------------------------------- #
#             GLOBAL VARIABLES             #
# ---------------------------------------- #

# load files
df = pd.read_pickle('data/df_happiness.pkl')

df['regional_indicator'].replace(to_replace=[None], value = 'Other', inplace = True)

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
    # layout = 'wide',
    initial_sidebar_state = 'auto'
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
    default = ['Brazil', 'Argentina', 'Uruguay',
                'Greece', 'Germany',
                'Finland', 'Denmark', 'Switzerland',
                'Afghanistan', 'Zimbabwe', 'Rwanda']
)

if len(selected_countries):
    change_df(df[df.country.isin(selected_countries)])
else:
    change_df(df)


# Checkbox for sorting
sort = st.sidebar.checkbox(
    'Ascending order of happiness', 
    value = True)

# Column selector
selected_col  = st.sidebar.selectbox(
    'Select the X column to the Scatter',
    options = df.columns[3:-2]
    )


# ---------------------------------------- #
#              PAGE ELEMENTS               #
# ---------------------------------------- #
 

scatter = render_scatter(df_aux, st, sort)


# c2.markdown('#### Map of Mean Happiness Index Score by Country')

line_chart = render_line(df_aux, st)

scatter2 = render_scatter_2(df_aux, selected_col, st)

map_chart = render_map(df, st)

st.dataframe(df.head())