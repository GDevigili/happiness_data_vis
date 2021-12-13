import plotly.express as px
from utils import *

blue = '#3177CD'
yellow = '#FFAD01'
light_gray = '#E0E0E0'
gray = '#b7b7b7'
green = '#7AE582'

def scatter_chart(df, ascending = False):

    fig = px.scatter(
        # data
        df.sort_values(['happiness_score'], ascending = ascending), 
        x = 'happiness_score', 
        y = 'country',

        # color
        color = 'highlight',
        color_discrete_map={
                'Other years': light_gray,
                2020: blue,
                2021: yellow,
                'Mean score': green
            },

        # height
        height = 200 + len(df.country.unique()) * 20,

        # hover data
        hover_data = ['country', 'year', 'happiness_score'],
        
        # title and labels
        title = 'World Happiness Report 2007-2021: Happiness Index Score by Country',
        labels = {
            'happiness_score': 'Happiness Index Score',
            'country': ''
        },

        # marginal_x = 'histogram'
    )

    fig.update_yaxes(
        tickvals = df.country.unique(),              # make a line for each country
        range = [-.8, len(df.country.unique())+.5],
        gridcolor = gray
    )            

    fig.update_xaxes(
        tickwidth = 1,
        range = (2, 8.2), 
        linecolor = gray
    )

    fig.update_traces(
        marker = {
            'size': 12,
            'opacity':0.7,
            'line':{'width':1, 'color': gray},
        }
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
            yanchor = 'bottom', 
            title = '',
            y = 1.0,
            traceorder = 'reversed'
        ),

    )

    return fig