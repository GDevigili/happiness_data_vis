import streamlit as st
import pandas as pd
from source.scatter_chart import *

def get_df_mean(df):
    df_mean = pd.DataFrame(columns=['country', 'happiness_score'])
    for country in df['country'].unique():
        new_col = df[df['country'] == country].groupby('country').mean()
        new_col['country'] = country
        df_mean = df_mean.append(new_col[['country', 'happiness_score']])

    return df_mean