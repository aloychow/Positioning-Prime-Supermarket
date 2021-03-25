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
                
                dbc.NavLink("Sentiment Analysis", href="/apps/1"),
                
                dbc.DropdownMenu([
                    dbc.NavLink("2.1",
                                href="/apps/2.1",
                                active="exact"),
                    dbc.NavLink("2.2",
                                href="/apps/2.2",
                                active="exact")],
                    label="2",
                    nav=True,
                ),

                dbc.DropdownMenu([
                    dbc.NavLink("3.1", href="/apps/sentiment_analysis/analysis_reddit"),
                    dbc.NavLink("3.2", href="/apps/sentiment_analysis/sentiment_analysis_twitter"),
                ],
                    label="Sentiment Analysis",
                    nav=True,
                ),
            ],
            vertical=True,
            # pills=True,
            # style="#44484A"
        ),
    ],
    style=SIDEBAR_STYLE,
)
