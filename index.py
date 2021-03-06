import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app, server

from assets.styles import CONTENT_STYLE
from sidebar import sidebar

from apps import homepage
from apps.sentiment import sentiment
from apps.association import association
from apps.ocr import ocr
from apps.rcnn import rcnn

## ---------- Creating layout using dash and bootstrap ---------- ##
app.layout = dbc.Container([
    html.Div([
        dcc.Location(id='url', refresh=False),

        sidebar,

        # Store page layout here
        html.Div(id='page-content', children=[])
    ], style=CONTENT_STYLE)
])


## ---------- Callback section: connecting components ---------- ##

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/homepage':
        return homepage.layout
    if pathname == '/apps/sentiment':
        return sentiment.layout
    if pathname == '/apps/association':
        return association.layout
    if pathname == '/apps/ocr':
        return ocr.layout
    if pathname == '/apps/rcnn':
        return rcnn.layout

    else:
        return homepage.layout


if __name__ == '__main__':
    app.run_server(debug=False, port=3000)
