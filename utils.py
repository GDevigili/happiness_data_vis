import streamlit as st
import pandas as pd
from charts import *

def df_mean(df, value_col, group_col):
    for col in df[group_col].unique():
        return df[df[group_col] == col].groupby(group_col)[value_col].mean()


def render_scatter(df, sort = False):
    return st.plotly_chart(scatter_chart(df, ascending = sort))