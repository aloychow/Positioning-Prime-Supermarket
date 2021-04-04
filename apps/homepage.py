import dash_bootstrap_components as dbc
import dash_html_components as html

import id_factory as idf
from app import app

id_start = idf.init_id('homepage')

layout = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col([
            html.H2("Prime Supermarket", className='text-center text-white font-weight-normal p-4')
        ])
    ]),

    dbc.Row([
        html.H5('Prime Supermarket has been facing increasing competition from both direct and indirect competitors. '
                'To continue thriving, Prime Supermarket has to be able to adapt by growing its business and maintaining '
                'market share.'
                'Prime Supermarket mainly operates through physical stores (24 outlets as of '
                '2021). Hence, we will focus on tackling their offline business by employing the use of other data '
                'analytics methods to provide deeper analysis for Prime Supermarket. We aim to take advantage of '
                'analytics software to maximise Prime’s market share and better position Prime in this competitive '
                'landscape - through:'
                ,
                className='text-center text-white font-weight-normal p-4'),

    ]),

    dbc.Row([
        dbc.Col([
            html.H5('• Customer acquisition and retention',
                    className='text-center text-white font-weight-normal')
        ])
    ]),

    dbc.Row([
        dbc.Col([
            html.H5('• Profit-maximisation',
                    className='text-center text-white font-weight-normal'
                    )
        ])
    ]),

    dbc.Row([
        dbc.Col([
            html.H5('• Cost-restructuring',
                    className='text-center text-white font-weight-normal'
                    )
        ])
    ]),

    html.Br(),
    html.Br(),
    html.Br(),


    dbc.Row([
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardImg(src=app.get_asset_url('sentiment.png'),
                                style={'height': '70%', 'width': '70%'}, className='center', top=True),
                    dbc.CardBody(
                        [
                            html.H4("Sentiment Analysis", className="text-white"),
                            html.P(
                                "Analyses sentiment of  Prime Supermarket feedback.",
                                className="card-text",
                            ),

                            html.Br(),
                            html.Br(),
                            html.Br(),
                            # dbc.Button("Read More", color="primary"),
                        ]
                    ),
                ]
            )
        ]),

        dbc.Col([
            dbc.Card(
                [
                    dbc.CardImg(src=app.get_asset_url('association.png'),
                                style={'height': '70%', 'width': '70%'}, className='center', top=True),
                    dbc.CardBody(
                        [
                            html.H4("Association Rules", className="text-white"),
                            html.P(
                                "Used to optimise positioning of grocery produce.",
                            ),
                            html.Br(),
                            # dbc.Button("Read More", color="primary"),
                        ]
                    ),
                ]
            )
        ]),

        dbc.Col([
            dbc.Card(
                [
                    dbc.CardImg(src=app.get_asset_url('neuralnetwork.png'),
                                style={'height': '70%', 'width': '70%'}, className='center', top=True),
                    dbc.CardBody(
                        [
                            html.H4("Neural Networks", className="text-white"),
                            html.P(
                                "Used to automate data collection for further analysis.",
                            ),
                            html.Div(
                                "• OCR",
                            ),
                            html.Div(
                                "• YOLO",
                            ),
                            html.Br(),
                            # dbc.Button("Read More", color="primary"),
                        ]
                    ),
                ]
            )
        ])
    ]),
])
