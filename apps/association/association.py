import pathlib

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import requests
from dash.dependencies import Input, Output

# Import dataset
# Retrieve path
PATH = pathlib.Path(__file__).parent.parent
DATA_PATH = PATH.joinpath("../datasets").resolve()  # Change path to datasets

# Importing candlestick pattern dataset
association = str(DATA_PATH) + '/association.csv'
association_table = pd.read_csv(association, header=0, index_col=0, squeeze=True)

import id_factory as idf
from app import app

id_start = idf.init_id('association')

layout = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col([
            html.H2("Association Rules", className='text-center text-white font-weight-normal p-4')
        ])
    ]),

    html.Br(),

    dbc.Card(
        [
            dbc.CardHeader(html.H4("Problem Statement", className="text-white text-center")),
            dbc.CardImg(src=app.get_asset_url('association.png'),
                        style={'height': '30%', 'width': '30%'}, className='center', top=True),
            dbc.CardBody(
                [

                    html.H5(
                        'To ensure Prime Supermarket has an optimal floor plan and layout for shopping, association '
                        'rules can be used to build recommender systems and allow for optimal placing of products '
                        'purchased in tandem.',
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
                        'Association rules will help us determine the products customers often buy in tandem. Baskets '
                        'of products will be formed based on the minimum confidence, support and lift that we '
                        'specify. We will be using a dataset which contains the list of products purchased at '
                        'supermarkets by different families in Brazil to emulate Singapore’s supermarket transaction '
                        'history. ',
                        className="card-text",
                    ),

                    html.Br(),

                    html.H5(
                        'The threshold of the sentiment analysis is set to ±0.2. If the compound score of a review is '
                        'greater than 0.2, the review is considered positive. If the score is less than -0.2, '
                        'the review is negative.',
                        className='card-text'
                    ),

                    html.Br(),

                    html.Div(
                        "Negative: Score < -0.2",
                    ),
                    html.Div(
                        "Neutral: Score between -0.2 and 0.2",
                    ),
                    html.Div(
                        "Positive: Score > 0.2",
                    ),
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

                    html.H5(
                        'We determine the percentage ratio of positive and negative reviews. We then conduct word '
                        'review based on positive and negative feedback, to determine what to continue doing and what '
                        'to improve on.',
                        className="card-text",
                    ),

                    html.Br(),

                    html.H5(
                        'The threshold of the sentiment analysis is set to ±0.2. If the compound score of a review is '
                        'greater than 0.2, the review is considered positive. If the score is less than -0.2, '
                        'the review is negative.',
                        className='card-text'
                    ),

                    html.Br(),

                    html.Div(
                        "Negative: Score < -0.2",
                    ),
                    html.Div(
                        "Neutral: Score between -0.2 and 0.2",
                    ),
                    html.Div(
                        "Positive: Score > 0.2",
                    ),
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
            html.H3('Lift')
        ])
    ]),
    html.Br(),

    dbc.Row([
        dbc.Col([
            dcc.RangeSlider(
                id=idf.gen_id(id_start, 'lift'),
                min=0,
                max=2.5,
                step=0.1,
                value=[0, 2.5],
                marks={
                    0: {'label': '0', 'style': {'color': '#77b0b1'}},
                    0.5: {'label': '0.5'},
                    1: {'label': '1'},
                    1.5: {'label': '1.5'},
                    2: {'label': '2'},
                    2.5: {'label': '2.5', 'style': {'color': '#f50'}}
                }
            ),
            html.Br(),

            html.Div(id=idf.gen_id(id_start, 'table')),
        ])
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            html.H3('Support')
        ])
    ]),
    html.Br(),

    dbc.Row([
        dbc.Col([
            dcc.RangeSlider(
                id=idf.gen_id(id_start, 'support'),
                min=0,
                max=1,
                step=0.05,
                value=[0, 1],
                marks={
                    0: {'label': '0', 'style': {'color': '#77b0b1'}},
                    0.2: {'label': '0.2'},
                    0.4: {'label': '0.4'},
                    0.6: {'label': '0.6'},
                    0.8: {'label': '0.8'},
                    1: {'label': '1', 'style': {'color': '#f50'}}
                }
            ),
            html.Br(),

            html.Div(id=idf.gen_id(id_start, 'table')),
        ])
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            html.H3('Confidence')
        ])
    ]),
    html.Br(),

    dbc.Row([
        dbc.Col([
            dcc.RangeSlider(
                id=idf.gen_id(id_start, 'confidence'),
                min=0,
                max=1,
                step=0.05,
                value=[0, 1],
                marks={
                    0: {'label': '0', 'style': {'color': '#77b0b1'}},
                    0.2: {'label': '0.2'},
                    0.4: {'label': '0.4'},
                    0.6: {'label': '0.6'},
                    0.8: {'label': '0.8'},
                    1: {'label': '1', 'style': {'color': '#f50'}}
                }
            ),
        ])
    ]),

    html.Br(),

    # Ticker entry box
    dbc.Row([
        dbc.Col([
            dbc.Row([
                html.Div("Antecedent:", className='text-white')
            ]),
            dbc.Row([
                dbc.Input(id=idf.gen_id(id_start, 'antecedent'), value='', type='text', bs_size='md')
            ], style={"width": "90%"})
        ]),

        # Show less dropdown selection
        dbc.Col([
            dbc.Row([
                html.Div("Consequent:", className='text-white')
            ]),
            dbc.Row([
                dbc.Input(id=idf.gen_id(id_start, 'consequent'), value='', type='text', bs_size='md')
            ], style={"width": "90%"})
        ]),

    ], justify='center', no_gutters=True),

    html.Br(),

    html.Div(id=idf.gen_id(id_start, 'table')),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br()

])


# Callbacks

@app.callback(
    [Output(component_id=idf.gen_id(id_start, 'table'), component_property='children')],
    [Input(component_id=idf.gen_id(id_start, 'lift'), component_property='value'),
     Input(component_id=idf.gen_id(id_start, 'support'), component_property='value'),
     Input(component_id=idf.gen_id(id_start, 'confidence'), component_property='value'),
     Input(component_id=idf.gen_id(id_start, 'antecedent'), component_property='value'),
     Input(component_id=idf.gen_id(id_start, 'consequent'), component_property='value')]
)
def update_table(lift, support, confidence, antecedent, consequent):
    # table = pd.DataFrame(columns=['Antecedent', 'Consequent', 'Lift', 'Support', 'Confidence'])  # Create empty dataframe

    final_range = []

    table = association_table[(lift[0] <= association_table['Lift']) & (association_table['Lift'] <= lift[1])]

    table = table[(support[0] <= table['Support']) & (table['Support'] <= support[1])]

    table = table[(confidence[0] <= table['Confidence']) & (table['Confidence'] <= confidence[1])]

    table = table[table['Antecedent'].str.contains(antecedent)]

    table = table[table['Consequent'].str.contains(consequent)]

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

    return [table]
