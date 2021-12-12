import plotly.express as px
from utils import *

def scatter_chart(df, ascending = False):

    fig = px.scatter(
    df.sort_values(['happiness_score'], ascending = ascending), 
    x = 'happiness_score', 
    y = 'country',
    color = 'highlight',
    height = 200 + len(df.country.unique()) * 20,
    hover_data = ['country', 'year', 'happiness_score'],
    color_discrete_map={'none': 'white'}
    )

    fig.update_yaxes(
        tickvals = df.country.unique(),              # make a line for each country
        range=[-.5,len(df.country.unique())+.5]
    )            

    fig.update_xaxes(
        tickwidth = 1,
        range = (1, 8.2)
    )

    fig.update_traces(
        marker = {
            'size': 12,
            'opacity':0.5,
            'line':{'width':1, 'color': 'DarkSlateGrey'}
        }
        
    )

    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)'       # make the background transparent
        # 'paper_bgcolor': 'rgba(0, 0, 0, 0)'
    }
    )

    return fig