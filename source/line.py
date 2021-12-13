import plotly.express as px
from source.utils import *
import streamlit as st

gray = '#b7b7b7'

def render_line(df, st_col):
    fig = px.line(
        # data
        df,
        x = 'year',
        y = 'happiness_score',

        #color 
        color = 'country',

        # title and labels
        title = 'Happiness Index Score by Country <br> <sup>Happiness over time</sup>',
        labels = {
            'happiness_score': 'Happiness Index Score',
            'country': '',
            'year':  ''
        },

        # markers
        markers = True
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
            orientation = 'v'
        )
    )

    return st_col.plotly_chart(fig)
