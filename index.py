import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app, server

from assets.styles import CONTENT_STYLE
from sidebar import sidebar

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
        pass


if __name__ == '__main__':
    app.run_server(debug=False, port=3000)
