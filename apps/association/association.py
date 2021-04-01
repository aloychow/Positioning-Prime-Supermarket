import dash_bootstrap_components as dbc
import dash_html_components as html

import id_factory as idf
from app import app

id_start = idf.init_id('homepage')

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

    html.Br(),

])
