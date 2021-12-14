import streamlit as st
import pandas as pd
from source.main_chart import *

def df_mean_by_country(df):
    df_mean = pd.DataFrame(columns=['country', 'happiness_score'])
    for country in df['country'].unique():
        new_col = df[df['country'] == country].groupby('country').mean()
        new_col['country'] = country
        df_mean = df_mean.append(new_col[['country', 'happiness_score']])

    return df_mean

def df_mean_by_region(df):
    df_mean = pd.DataFrame(columns=['regional_indicator', 'happiness_score'])
    for region in df['regional_indicator'].unique():
        new_col = df[df['regional_indicator'] == region].groupby('regional_indicator').mean()
        new_col['regional_indicator'] = region
        df_mean = df_mean.append(new_col[['regional_indicator', 'happiness_score']])

    return df_mean

def df_mean(df, group_col, value_col):
    mean_list = []
    df_mean = pd.DataFrame(columns = [group_col, value_col])
    for col in df[group_col].unique():
        new_col = df[df[group_col] == col].groupby(group_col)[value_col].mean()
        mean_list.append(new_col[0])

    df_mean[group_col] = df[group_col].unique()
    df_mean[value_col] = mean_list
    
    return df_mean

def df_mean_by_year(df, group_col, value_col):
    mean_list = []
    df_mean = pd.DataFrame(columns = [group_col, value_col])
    for col in df[group_col].unique():
        new_col = df[df[group_col] == col].groupby([group_col, 'year'])[value_col].mean()
        mean_list.append(new_col[0])

    df_mean[group_col] = df[group_col].unique()
    df_mean[value_col] = mean_list
    
    return df_mean