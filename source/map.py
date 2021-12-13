import plotly.express as px
from utils import *
import pycountry
import streamlit as st

blue = '#3177CD'
yellow = '#FFAD01'
red = '#BF3100'
gray = '#E0E0E0'
dark_blue = '#201335'
light_blue = '#53F4FF'
green = '#7AE582'


def render_map(df):
    # get the mean df
    df_mean = get_df_mean(df)

    # transform the country names into ISO
    countries = {}

    for country in pycountry.countries:
        countries [country.name] = country.alpha_3

    df_mean['country_iso'] = [countries.get(country, 'Unknown code') for country in df_mean['country'].unique()]

    fig = px.choropleth(
        df_mean,
        locations = 'country_iso', 
        color = 'happiness_score',
        color_continuous_scale = px.colors.sequential.Aggrnyl
    )

    return st.plotly_chart(fig)

