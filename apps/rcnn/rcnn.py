import dash_bootstrap_components as dbc
import dash_html_components as html

import id_factory as idf
from app import app

id_start = idf.init_id('homepage')

layout = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col([
            html.H2("YOLO", className='text-center text-white font-weight-normal p-4'),
        
        html.H4("Aloysius Chow", className = 'text-center text-white font-weight-normal p-4'),
        ]),
    ]),

    html.Br(),

    dbc.Card(
        [
            dbc.CardHeader(html.H4("Problem Statement", className="text-white text-center")),
            dbc.CardImg(src=app.get_asset_url('neuralnetwork.png'),
                        style={'height': '30%', 'width': '30%'}, className='center', top=True),
            dbc.CardBody(
                [

                    html.H5(
                        'To ensure Prime Supermarket can better predict manpower needs and deploy manpower '
                        'efficiently, R-CNNs are used to automate people counting and predict future demand.',
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
                    dbc.CardImg(src=app.get_asset_url('yolo-compare.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),
                    dbc.CardImg(src=app.get_asset_url('yolo.png'),

                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

                    html.Br(),

                    html.H5(
                        'YOLO-v3 Framework, a state-of-the-art object detection algorithm, is used. It firstly '
                        'applies a single neural network to the whole image, which is used to produce individual cell '
                        'probabilities.',
                        className="card-text",
                    ),

                    dbc.CardImg(src=app.get_asset_url('yolo-layers.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

                    html.Br(),

                    html.H5(
                        'YOLO detects classes at layers 82, 94 and 106 respectively. This produces 3 bounding boxes '
                        'per layer, and the maximum probability of each class is found. The bounding boxes of the '
                        'detected class will be calculated offsetted from the anchors, and passed through the sigmoid '
                        'function.',
                        className='card-text'
                    ),

                    html.Br(),

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
            dbc.CardHeader(html.H4("Training the Model", className="text-white text-center")),
            dbc.CardBody(
                [
                    dbc.CardImg(src=app.get_asset_url('google-dataset.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

                    html.Br(),

                    html.H5(
                        'We used the OIDv4 repository to download images from Google\'s Open Images Dataset. We '
                        'download 10000 human-labelled images.',
                        className="card-text",
                    ),

                    dbc.CardImg(src=app.get_asset_url('yolo-txt-format.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

                    html.Br(),

                    html.H5(
                        'YOLO requires corresponding txt files for the bounding boxes in a specific format: class, '
                        'x_centre, y_centre, width, height. However, Google\'s txt file looks like: x_min, y_min, '
                        'x_max, y_max. We wrote a python script to convert the format from Google to YOLO.',
                        className='card-text'
                    ),

                    dbc.CardImg(src=app.get_asset_url('yolo-training.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

                    html.Br(),

                    html.H5(
                        'We tune specific parameters such as filters, max_batches, steps and batches. Hyperparameter '
                        'tuning is also possible for others such as activation function, learning rate, '
                        'angle and saturation. Following which, we applied trasnfer learning on an existing model, '
                        'darknet53 (uses weights).',
                        className='card-text'
                    ),

                    html.Br(),

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
                    dbc.CardImg(src=app.get_asset_url('supermarket-few.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

                    html.H5(
                        'We tried the model on fewer people.',
                        className="card-text",
                    ),

                    dbc.CardImg(src=app.get_asset_url('supermarket-many.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

                    html.H5(
                        'As well as many people.',
                        className="card-text",
                    ),

                    html.Br(),

                    html.Video(src=app.get_asset_url('supermarket-video.mp4'), controls=True,
                               style={'height': '100%', 'width': '100%'}),

                    html.H5(
                        'We also tested on actual camera footage.',
                        className="card-text",
                    ),

                    dbc.CardImg(src=app.get_asset_url('graph.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

                    html.H5(
                        'A simulation of the shoppers against time over 5 days.',
                        className="card-text",
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
