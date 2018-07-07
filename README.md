# btc_predictor
This project uses LSTM to predict BTC prices
## Overview
After playing with RNN LSTM for synthetic text generation as well as image spoofing I discovered there is a usage for RNN LSTM in prediction.  I thought it might be fun to try to build a bitcoin market predictor using RNN LSTM to see how well it does.  
 
My initial hypothesis was it would not do well based on BTC’s market volatility.  I was surprised by the results. 
 
To conduct the experiment, I used my NVIDIA Jetson TX2 GPU computer and the software is a combination of python’s, numpy, keras, and tensorflow. 
 
Lucky for me Coindesk has an API for BTC current and historical market data.  My training data for the model uses a range from 9/1/2013 -> 12/31/2017 and the test data was from 2/1/2018 -> 3/12/2018.   I ensured there was no overlap between the training data and the test data.
 
It takes ~ 3 1/2 minutes to generate the results which you can see for yourself in the  figure below.  

## Results

This is output from the program

![BTC Price prediction](btc_price_prediction.png?raw=true "BTC Price Prediction")


##  The code
To generate the bitcoin test data, I forked a project that enables access to a number of crypto currency APIs

test_data_btc.py is a program that geneates my test and training data

Bitcoin Price API
----------------------------------------------------------------------


### Coindesk

The Coindesk class offers a much richer price interface:

    get_current_price(currency='USD')
    get_past_price(date)
    get_historical_data_as_dict(start='2013-09-01', end=None)
    get_historical_data_as_list(start='2013-09-01', end=None)

`get_current_price` and `get_past_price` both return `Decimal` objects.

`get_current_price` takes in an optional parameter specifying the currency.

The dates for all functions must be in the form 'YYYY-MM-DD'.

`get_historical_data_as_dict` will return a dictionary of the following format:

    {'2014-10-20': 400.00, '2014-10-21': 301.99}

Remember that these date/prices will not be in any given order.

`get_historical_data_as_list` will return a list of dictionaries, correctly
sorted by date from start to end.

    [
        {'date': 'YYYY-MM-DD', 'price': 300.00},
        {'date': 'YYYY-MM-DD', 'price': 301.00 }
    ]

