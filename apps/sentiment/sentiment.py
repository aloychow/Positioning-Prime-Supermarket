import pathlib

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import requests
from dash.dependencies import Input, Output

import id_factory as idf
from app import app

id_start = idf.init_id('sentiment')

# Import dataset
# Retrieve path
PATH = pathlib.Path(__file__).parent.parent
DATA_PATH = PATH.joinpath("../datasets").resolve()  # Change path to datasets

# Importing candlestick pattern dataset
sentiment = str(DATA_PATH) + '/Sentiment_Reviews.csv'
sentiment_table = pd.read_csv(sentiment, header=0, index_col=0, squeeze=True)

layout = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col([
            html.H2("Sentiment Analysis", className='text-center text-white font-weight-normal p-4')
        ])
    ]),

    html.Br(),

    dbc.Card(
        [
            dbc.CardHeader(html.H4("Problem Statement", className="text-white text-center")),
            dbc.CardImg(src=app.get_asset_url('sentiment.png'),
                        style={'height': '30%', 'width': '30%'}, className='center', top=True),
            dbc.CardBody(
                [

                    html.H5(
                        'Prime Supermarket may not have a way to track their current performance and customer '
                        'satisfaction using their reviews. Being able to identify problematic areas will be '
                        'beneficial for Prime and give them a competitive advantage on possible solutions to '
                        'implement.',
                        className="card-text",
                    ),

                ]
            ),
            dbc.CardFooter(''),
        ],
        color='success',
        outline=True
    ),

    html.Br(),
    html.Br(),

    dbc.Card(
        [
            dbc.CardHeader(html.H4("Method", className="text-white text-center")),
            dbc.CardBody(
                [

                    html.H5(
                        'We can determine:',
                        className="card-text",
                    ),

                    html.H5(
                        "1. Negative words associated with Prime supermarket based on reviews ",
                    ),
                    html.H5(
                        "2. Positive words that result to customer satisfaction based on reviews",
                    ),
                    html.H5(
                        "3. Percentages between the positive reviews against the negative reviews",
                    ),

                    dbc.CardImg(src=app.get_asset_url('sentiment-range.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),
                ]
            ),
            dbc.CardFooter(''),
        ],
        color='warning',
        outline=True
    ),

    html.Br(),
    html.Br(),

    dbc.Card(
        [
            dbc.CardHeader(html.H4("Insights", className="text-white text-center")),
            dbc.CardBody(
                [

                    dbc.CardImg(src=app.get_asset_url('sentiment-percentage.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

                    html.H5(
                        'Prime Supermarket can identify the overall percentage of positive reviews against its '
                        'negative reviews for that period, giving an overview of whether customers are satisfied '
                        'during that period. Prime can conduct this analysis for each month and monitor the '
                        'performance of their products and services throughout the year.',
                        className='card-text'
                    ),

                    html.Br(),

                ]
            ),
            dbc.CardFooter(''),
        ],
        color='danger',
        outline=True
    ),

    html.Br(),
    html.Br(),

    dbc.Row([
        dbc.Col([
            html.H3('Rating Range')
        ])
    ]),
    html.Br(),

    dbc.Row([
        dbc.Col([
            dcc.RangeSlider(
                id=idf.gen_id(id_start, 'slider'),
                min=1,
                max=5,
                step=1,
                value=[1, 5],
                marks={
                    1: {'label': '1', 'style': {'color': '#77b0b1'}},
                    2: {'label': '2'},
                    3: {'label': '3'},
                    4: {'label': '4'},
                    5: {'label': '5', 'style': {'color': '#f50'}}
                }
            ),
            html.Br(),

            html.Div(id=idf.gen_id(id_start, 'table')),
        ])
    ]),

    html.Br(),

])


# Callbacks

@app.callback(
    [Output(component_id=idf.gen_id(id_start, 'table'), component_property='children')],
    [Input(component_id=idf.gen_id(id_start, 'slider'), component_property='value')]
)
def update_table(range2):
    table = pd.DataFrame(columns=['Review', 'Rating', 'Sentiment', 'Type'])  # Create empty dataframe

    final_range = []

    for i in range(range2[0], range2[1] + 1):
        final_range.append(i)

    table = sentiment_table[sentiment_table['Rating'].isin(final_range)]

    table = dash_table.DataTable(
        id="table",

        columns=[
            {"name": i, "id": i} for i in table.columns
        ],
        data=table.to_dict('records'),
        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'fontWeight': 'bold',
        },

        style_table={'overflowX': 'scroll'},

        style_cell={
            'backgroundColor': 'rgb(50, 50, 50)',
            'color': 'white',
            'padding': '10px',
            'textAlign': 'left',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
            'maxWidth': 0
        },

        style_as_list_view=True,

        tooltip_data=[
            {
                column: {'value': str(value), 'type': 'markdown'}
                for column, value in row.items()
            } for row in table.to_dict('records')
        ],
        sort_action="native",
        sort_mode="multi",
        tooltip_duration=None,
        page_size=10
    )

    print(range)

    return [table]
