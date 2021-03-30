import dash_html_components as html
import dash_bootstrap_components as dbc

from assets.styles import SIDEBAR_STYLE

sidebar = html.Div(
    [
        html.H5("Supermarket Analysis", className="text-center text-white"),
        html.Hr(style={
            'background-color': 'white'
        }),
        # html.P(
        #     "Table of Contents", className="lead"
        # ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/apps/homepage"),

                dbc.NavLink("Sentiment Analysis", href="/apps/sentiment"),

                dbc.NavLink("Association Rules", href="/apps/association"),

                dbc.NavLink("Optical Character Recognition", href="/apps/ocr"),

                dbc.NavLink("Fast Region CNN", href="/apps/rcnn"),

            ],
            vertical=True,
            # pills=True,
            # style="#44484A"
        ),
    ],
    style=SIDEBAR_STYLE,
)
