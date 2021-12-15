import plotly.express as px
from source.utils import *
import streamlit as st
import statsmodels

blue = '#3177CD'
yellow = '#FFAD01'
light_gray = '#E0E0E0'
gray = '#b7b7b7'
green = '#7AE582'

def render_scatter_2(df, x_col, st_col):

    color_by = 'country'
    if len(df['country'].unique()) > 10:
        color_by = 'regional_indicator'

    fig = px.scatter(

        # data
        df,
        x = x_col,
        y = 'happiness_score',

        # color
        color = color_by,

        # trendline
        trendline = 'ols'
        
    )

    fig.update_yaxes(
        gridcolor = gray
    )

    fig.update_layout(
        # background
        {
            'plot_bgcolor': 'rgba(0, 0, 0, 0)'
        },

        # fonts
        font_family = 'Courier New',
        title_font_family = 'Arial',
        
        # legend
        legend = dict(
            orientation = 'h',
            title = '',
        ),

    )

    return st_col.plotly_chart(fig)