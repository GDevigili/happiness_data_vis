import plotly.express as px
from utils import *

def scatter_chart(df, ascending):
    # df_means = 
    df.sort_values(by = None, ascending = ascending)

    fig = px.scatter(
    df, 
    x = 'happiness_score', 
    y = 'country',
    color = 'highlight',
    height = 200 + len(df.country.unique()) * 20,
    hover_data = ['country', 'year', 'happiness_score'],
    color_discrete_map={'none': 'white'}
    )

    fig.update_yaxes(
        tickvals = df.country.unique(),              # make a line for each country
        
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