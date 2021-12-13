import streamlit as st
import pandas as pd
from charts import *
import plotly.subplots 

def get_df_mean(df, value_col, group_col):
    for col in df[group_col].unique():
        return df[df[group_col] == col].groupby(group_col)[value_col].mean()


def render_scatter(df, sort = False):
    colors = {
        '2020': '#3177CD',
        '2021': '#051B33',
        'Other years': '#E7E7E7',
        'Mean': '#FFAD01'
    }

    df_others = df[~df['year'].isin([2020, 2021])]
    fig_others = scatter_chart(df_others, colors['Other years'], sort)

    df2020 = df[df['year'] == 2020]
    fig2020 = scatter_chart(df2020, colors['2020'], sort)

    df2021 = df[df['year'] == 2021]
    fig2021 = scatter_chart(df2021, colors['2021'], sort)

    # df_mean = get_df_mean(df, 'happiness_score', 'country')
    # scatter_chart(df_mean, colors['Mean'], sort)

    fig = plotly.subplots.make_subplots()
    fig.add_trace(fig_others)
    fig.add_trace(fig2020)
    fig.add_trace(fig2021)
    # fig.add_trace(df_mean)

    return fig