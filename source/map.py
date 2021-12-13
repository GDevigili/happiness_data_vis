import plotly.express as px
from source.utils import *
import pycountry
import streamlit as st

blue = '#3177CD'
yellow = '#FFAD01'
red = '#BF3100'
gray = '#E0E0E0'
dark_blue = '#201335'
light_blue = '#53F4FF'
green = '#7AE582'


def render_map(df, st_col):
    # get the mean df
    df_mean = get_df_mean(df)

    # transform the country names into ISO
    countries = {}

    for country in pycountry.countries:
        countries [country.name] = country.alpha_3

    # get mean by country
    df_mean['country_iso'] = [countries.get(country, 'Unknown code') for country in df_mean['country'].unique()]

    df_mean.rename(columns = {'happiness_score': 'Mean HIS'}, inplace=True)

    # generate the figure
    fig = px.choropleth(
        # data
        df_mean,
        locations = 'country_iso', 
        color = 'Mean HIS',

        # color
        color_continuous_scale = px.colors.sequential.Aggrnyl,

        # title and lables
        # label = {'happiness_score': 'Mean Happiness Index Score'}
    )

    fig.update_layout(
        legend = dict(
            orientation = 'h',
            yanchor = 'bottom',
            y = 1.0
        )
    )

    fig.update_layout(width = 500, height = 400)

    return st_col.plotly_chart(fig)

