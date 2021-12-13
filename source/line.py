import plotly.express as px
from source.utils import *
import streamlit as st

def render_line(df, st_col):
    fig = px.line(
        # data
        df,
        x = 'year',
        y = 'happiness_score',

        #color 
        color = 'country',

        # markers
        markers = True
    )

    return st_col.plotly_chart(fig)
