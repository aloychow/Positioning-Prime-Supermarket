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
            html.H2("Association Rules", className='text-center text-white font-weight-normal p-4'),
            html.H4("Alicia Chua", className = 'text-center text-white font-weight-normal p-4'),
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
                        "Product placement influences customers' shopping behaviour. By placing complementary products near each other, customers will find it easier to search for a complementary item. This will greatly enhance their shopping experience through increased convenience. Moreover, it also promotes the purchasing of complementary items, boosting sales for Prime. Given this in mind, we decided to use association rules to help Prime Supermarket find the most important complementary product pairings .",
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
                        "But before that, we have to organise the dataset to suit our analysis.",
                        className='card-text'
                    ),

                    html.H5(
                        "First, the dataset was originally in a long data format: ",
                        className='card-text'
                    ),

                    dbc.CardImg(src=app.get_asset_url('long_data.png'),
                        style={'height': '30%', 'width': '30%'}, className='center', top=True),

                    html.Br(),

                    html.H5(
                        "Thus, we first converted it into a wide data format. ",
                        className='card-text'
                    ), 
                    html.Br(),

                    html.H5(
                        "Next, we dropped these 3 columns as we felt that they were not relevant to Prime: ",
                        className='card-text'
                    ), 

                    dbc.CardImg(src=app.get_asset_url('droppedcols.png'),
                        style={'height': '40%', 'width': '40%'}, className='center', top=True), 

                    html.Br(),

                    html.H5(
                        "Lastly, we checked the top 5 most purchased items. High frequencies could hint that the products are often bought in tandem: ",
                        className='card-text'
                    ), 

                    dbc.CardImg(src=app.get_asset_url('top5.png'),
                        style={'height': '70%', 'width': '70%'}, className='center', top=True),
                    
                    html.Br(),

                    html.H5(
                        "We can see that basic food items and condiments are purchased the most often, probably because of their versatility. On the other hand, items which are purchased the least are often expensive and cater to a very niche audience. Examples include: ",
                        className='card-text'
                    ), 
                    dbc.CardImg(src=app.get_asset_url('low5.png'),
                        style={'height': '40%', 'width': '40%'}, className='center', top=True),
                    
                    html.Br(),   

                    html.H5(
                        "For our analysis, we set our minimum confidence and support to be = 0.4. The number of items in each basket has to be > 1 in order to ensure that there will be both antecendents and consequents. However, for this presentation, we will be playing around with other values as well. For the sake of simplicity in this presentation, we have limited the number of items in the basket to be = 2",
                        className='card-text'
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
                        "When minimum confidence = 0.4, minimum support = 0.4 and minimum lift = 1: ",
                        className="card-text",
                    ),

                    html.Br(),

                    html.H5(
                        "We can see that most of the items here are in the most frequently purchased graph shown earlier. Because lifts are greater than 1, we can say with confidence that the antecedent will boost the occurrence of the consequent. ",
                        className='card-text'
                    ),

                    html.Br(),

                    html.H5(
                        "Prime Supermarket can thus consider placing these items near each other. For example, placing the bread, condiments and baking section near each other could potentially save customers lots of time, and at the same time boosting sales of these items. ",
                        className='card-text'
                    ),

                    html.Br(),

                    html.H5(
                        "If you observe carefully, you'll realise that most of the items in these rules are considered as necessities. Thus, customers are likely to purchase these items regularly to restock their supply at home. Hence, Prime can consider placing these items at the back of the store so that customers have to navigate through the entire store to find them. The longer a customer stays in a shop, the higher the probability that he will purchase additional items.",
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
