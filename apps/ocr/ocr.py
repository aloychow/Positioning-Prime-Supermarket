import dash_bootstrap_components as dbc
import dash_html_components as html

import id_factory as idf
from app import app

id_start = idf.init_id('homepage')

layout = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col([
            html.H2("Optical Character Recognition", className='text-center text-white font-weight-normal p-4'),
            html.H4("Jie Sheng", className = 'text-center text-white font-weight-normal p-4'),
        ])
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
                        'Utilising optical character recognition as a feature in addition to association rules. By '
                        'utilising OCR on our receipts, we will be able to generate more data for the association '
                        'rules dataset.',
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
                        'Optical character recognition is a tool that converts images with text into machine-encoded '
                        'text. In general, the better the image quality (size, contrast, lightning) the better the '
                        'recognition result. The general steps taken during OCR are shown below:',
                        className="card-text",
                    ),

                    dbc.CardImg(src=app.get_asset_url('ocr1.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

                    html.Br(),

                    html.H5('Firstly, the OCR software will:'),

                    html.H5(
                        '1. Pre-Process Images. To Improve the chances of successful recognition, images are skewed, '
                        'rescaled, and cleaned. Colour is also converted from colour to a binary image (black and '
                        'white). ',
                        className='card-text'
                    ),

                    html.Br(),

                    html.H5(
                        '2.	Text Segmentation and Recognition. Actual text will be segmented out from blank spaces & '
                        'lines and will be further segmented into characters. This can be done by: ',
                        className='card-text'
                    ),

                    html.H5(
                        '     a)	Template matching - match each character image to the text template.',
                        className='card-text'
                    ),

                    html.H5(
                        'b)	Feature extraction - detect and extract features from the input character image and '
                        'compare it with the OCR’s predetermined features. '
                    ),

                    html.Br(),

                    html.H5('3.	Post-Processing. After characters are recognised and formed into words, the output can '
                            'be further processed by integrating dictionaries based on the language and create '
                            'algorithms based on the context of the image that we are ‘reading’ from. This will '
                            'generally increase the OCR software’s accuracy and allow us to extract our required '
                            'information.'),

                    html.Br(),

                    html.H3('Tessaract', className='text-white'),

                    html.H5('For this, we will be making use of Google’s open-source OCR program called Tesseract. '
                            'Tesseract also supports multiple languages which shows versatility of this concept. '
                            'Tesseract uses a two-pass approach by using recognised characters to identify characters '
                            'that have low confidence. Tesseract uses neural networks that are trained to recognise '
                            'words and text instead of just characters. '),

                    html.H3('Elaboration', className='text-white'),

                    html.H5('These are the general steps we are going to take to read our receipts using Tesseract '
                            'OCR. We will first pre-process images with OpenCV followed by passing through '
                            'Pytesseract for text recognition. '),

                    html.H4('Step 1: Pre-processing', className='text-white'),

                    html.H5('3 different methods were used to pre-process the images: '),
                    html.H5('1.	Greyscale - Standard monochromatic output.'),
                    html.H5('2.	Canny Edge Detection - Multi-stage algorithm to detect edges in the image. '),
                    html.H5('3.	Thresholding '),

                    html.Br(),

                    html.H5('Standard thresholding - For every pixel will be compared to a threshold value to '
                            'determine if it should be is black or white. '),

                    html.Br(),

                    html.H5('Otsu Binarization - Otsu\'s method automatically determines the most optimal threshold '
                            'value based on an image histogram.'),

                    html.Br(),

                    html.H5('Adaptive Thresholding - In previous cases, a standard global value is used as the '
                            'threshold. But in most cases due to lighting conditions, a standard value may not work. '
                            'Adaptive thresholding determines thresholds based on the pixel’s surrounding region. '),

                    dbc.CardImg(src=app.get_asset_url('ocr2.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

                    html.Br(),

                    html.H4('Step 2: Text Segmentation & Recognition', className='text-white'),

                    html.H5('After preprocessing, we will feed the preprocessed images into Tesseract for the text '
                            'segmentation and recognition. '),
                    html.H5('Tesseract has its own trained model which has been trained on more than 400,000 lines of '
                            'textual data with more than 4,500 different fonts. To ensure accuracy can be maintained, '
                            'we decided not to re-train Tesseract as we do not have the same scale/amount of data.'),

                    html.Br(),
                    html.H5('Below a visual representation of the text segmentation and recognition from Tesseract:'),

                    dbc.CardImg(src=app.get_asset_url('ocr3.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

                    html.Br(),

                    html.H4('Step 3: Post-processing', className='text-white'),

                    html.H5('Given the text output of the textual data, we will have to extract required information '
                            'and remove all the unnecessary text in the OCR output. Since we can see the bounding box '
                            'information, we can add more conditions and methods to select the boxes with our '
                            'required information. '),
                    html.H5('To identify the bounding box of items bought, we must first identify the standard rule '
                            'of how each receipt is fomatted. We can then further perform string processing using '
                            'Regular Expressions (Regex) to get a list of items bought in a single receipt.  '),

                    html.Br(),
                    html.H5('Below are the results from this receipt after passing the receipt through our pipeline:'),

                    dbc.CardImg(src=app.get_asset_url('ocr4.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

                    dbc.CardImg(src=app.get_asset_url('ocr5.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

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

                    html.H5(
                        'The exact algorithms and rules will not work for different receipts with different formats. '
                        'Thus, this method is not scalable for different companies as they all have different formats '
                        'for their receipts. For Prime, using our own receipt, we have written the rules required to '
                        'extract all the items bought in the same reciept.',
                        className="card-text",
                    ),

                    html.Br(),

                    html.H5(
                        'Here are the results:',
                        className="card-text",
                    ),

                    html.Br(),

                    html.H5(
                        'Receipt 1',
                        className="card-text",
                    ),

                    dbc.CardImg(src=app.get_asset_url('ocr6.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),

                    html.Br(),

                    html.H5(
                        'Receipt 2',
                        className="card-text",
                    ),

                    dbc.CardImg(src=app.get_asset_url('ocr7.png'),
                                style={'height': '100%', 'width': '100%'}, className='center', top=True),


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
