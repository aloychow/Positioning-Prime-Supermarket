# Positioning Prime

The Covid-19 pandemic has led to many firms requiring restructuring, with those that failed to adapt, closing down. Prime Supermarket, which is a supermarket chain in Singapore and one which does not utilise technologies (such as online shopping), will find it hard to tide through the falling demand of physical shopping. As such, my group and I have decided to utilise analytical tools to bolster Prime's situation.
View and try out the [Prime Dashboard application](https://aloysius-portfolio.webflow.io/project/repositioning-prime).

## Our Three-Pronged Approach
To continue thriving, Prime Supermarket has to be able to adapt by growing its business and maintaining market share. Prime Supermarket mainly operates through physical stores (24 outlets as of 2021). Hence, we will focus on tackling their offline business by employing the use of other data analytics methods to provide deeper analysis for Prime Supermarket. We aim to take advantage of analytics software to maximise Prime’s market share and better position Prime in this competitive landscape - through:
1. Customer acquisition and retention
2. Profit-maximisation
3. Cost-restructuring
> "Prime Supermarket has been facing increasing competition from both direct and indirect competitors. "
‍
### 1) Customer Acquisition and Retention
To improve customer acquisition and retention, we looked at 2 aspects:
1. Sentiment Analysis (Prime Reviews)
2. Association Rules (Recommendation Engine)
‍

**Sentiment Analysis** of reviews allowed us to understand the overall general sentiment of Prime. We could then utilise these results to understand user issues regarding factors such as quality of food, price, convenience and more. This helped us identify various factors of improvement for Prime.
‍

**Association Rules** utilising a dataset which contained food items commonly bought together allowed us too build a dynamic recommendation engine to search for highly correlated food items. In the example below, you can toggle the lift, support, confidence, as well as set the antecedent and consequent. Looking below, we can set specific thresholds and understand how to position and place food items.
For example, if people who bought bananas commonly bought chocolate powder, we are able to place them close by to increase the likelihood of purchasing. Conversely, if we observe a very strong correlation between baby formula and diapers, we can strategically place them at opposite ends of the mart, to entice shoppers into impulse purchases when walking through.
‍
### 2) Profit Maximisation
To improve profit maximisation, we want to understand how often , what, and when to stock food items. Utilising optical character recognition as a feature in addition to association rules. By utilising OCR on our receipts, we will be able to generate more data for the association rules dataset.
For this, we will be making use of Google’s open-source OCR program called Tesseract. Tesseract also supports multiple languages which shows versatility of this concept. Tesseract uses a two-pass approach by using recognised characters to identify characters that have low confidence. Tesseract uses neural networks that are trained to recognise words and text instead of just characters. This will allow us to keep track of our products better to prevent oversupply and ensure stock.
‍

**Optical Character Recognition**
‍
### 3) Cost Restructuring
To ensure Prime Supermarket can better predict manpower needs and deploy manpower efficiently, R-CNNs are used to automate people counting and predict future demand.
YOLO Framework, a state-of-the-art object detection algorithm, is used. We will run videos of security camera footage through our real-time human detection model, whereby it will count the number of shoppers and forecast demand. You can view the real-time video detection here.
‍

**YOLO R-CNN**

We can plot the number of shoppers over time across different days, periods, accounting for festivals like Christmas. This allows us to deploy manpower more efficiently to aid cost savings, and prevent understaffing. For example, as the shoppers fall around 2pm, more staff could take their lunch break then. During the period before Christmas, if we observe higher demand in the past, we can increase the staff proportionally.
‍

Simulated Forecast of Shoppers Over Time
‍
With these features, we hope to aid Prime Supermarket in its growth and development. Through our three-pronged approach, Prime will be better ready to endure the tough times ahead.
