# AMLI Project - Bitcoin Price Prediction

 > This is a final project from Google Applied Machine Learning Intensive (AMLI) in summer 2019. 

 > Using machine learning (ML) techniques and given the Bitcoin historical data and sentiment analysis of relevant Reddit and Twitter posts, the model could predict the trend and the exact price of Bitcoin.

 > Keywords: applied machine learning, Bitcoin, cryptocurrency, price prediction, RNN, sentiment analysis

## Table of Contents

- [Getting Started](#getting-started)
- [Model Inputs](#model-inputs)
- [Model](#model)
- [Results](#results)
- [Future Steps](#future-steps)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)
- [References](#references)

## Getting Started

Code is intended to work with Python 3.6.x and Jupyter Notebook, or Google Colaboratory.

### Prerequisites
You need to download the packages needed for the code. Here is the way to download it:
```
pip install <package>
```

### Structures
There are four folders: `bitcoin`, `model`, `reddit`, and `twitter`. In each folder, the structure is as follow:

    ├── folder name                   
    |   ├── bin         # script files (ended with .py)
    |   ├── data             # dataset (ended with .csv or .xlsx)
    |   └── nb               # Jupyter Notebook (ended iwth .ipynb)

## Model Inputs
The model inputs come from three sources: Bitcoin historical data, sentiment analysis of Tweets, and sentiment analysis of Reddit posts.

### Bitcoin Historical Data
- **Download latest historical data**
To get the latest data for Bitcoin price and other features, you could go to [Bitcoin Core Charts](https://charts.bitcoin.com/btc/) and manually download the 39 files. Here is how to download them:
![Recordit GIF](http://g.recordit.co/61NpgDWg5I.gif)

An alternative way would be automating the web browser and download them. To do this, you need Selenium and corresponding web browser. The project uses Firefox version 40.0.3.
After successfully downloading them, you can run `bitcoin_data.py` in `bitcoin/bin`. It will download 39 files about Bitcoin price to `bitcoin/data/bitcoin_data`.

- **Use existing dataset**
In the `bitcoin/data/bitcoin_data` folder, there are 39 files ended with `.csv`. The latest data is July 29, 2019.

- **Merge data into one file**
Run `Merge_Data.ipynb` in `bitcoin/nb`, and it will generate a excel file called `bitcoin_merged.xlsx` in  `bitcoin/data`.

- Optional
If you are also interested in feeding the historical price of Litecoin or Ethereum to the model, you can run the corresponding code blocks in `Merge_Data.ipynb` and get `litecoin_data.csv` and `ethereum_data.csv` .

### Twitter
- **GetOldTweets3** 
This is an improvement fork of another project GetOldTweets. [GetOldTweets](https://github.com/Jefferson-Henrique/GetOldTweets-python) is a tweet scraping package that bypasses Twitter's offical API's general limitations especially when it comes to time constraints. [GetOldTweets3](https://pypi.org/project/GetOldTweets3/) fixes minor known issues with the original module, provides additional features such as number of retweets, and outputs the data as a csv more cleanly.

- **Installation**
To get historical Twitter data, you simply have to install the package through your local machine's command line: `pip install GetOldTweets3`

- **Export Data**
GetOldTweets3 exports tweets to a specified csv file called `output_got.csv` by default.

- **Query Examples**    
Example 1 - Get tweets by query search:  
`GetOldTweets3 --querysearch "europe refugees" --maxtweets 10`  

Example 2 - Get the last 10 top tweets by username:  
`GetOldTweets3 --username "barackobama" --toptweets --maxtweets 10`  

Example 3 - Get tweets by the username and bound dates (until date is not included):  
`GetOldTweets3 --username "barackobama" --since 2015-09-10 --until 2015-09-12 --maxtweets 10`  

Example 4 - Get tweets by several usernames:  
`GetOldTweets3 --username "BarackObama,AngelaMerkeICDU" --usernames-from-file userlist.txt --maxtweets 10`  

Example 5 - Get tweets by language:  
`GetOldTweets3 --querysearch "bitcoin" --lang cn --maxtweets 10`  

See [GetOldTweets3](https://pypi.org/project/GetOldTweets3/) for additional Twitter criteria.

### Reddit
### Sentiment Analysis

## Model
### Recurrent Neural Network (RNN) 
Open `Bitcoin_Price_Prediction.ipynb` in `model/nb` and follow the instructions to run the model.

### Echo State Network (ESN)
ESN is a type of RNN, and it is well adapted for handling chaotic time series. It has a sparsely connected hidden layer (with typically 1% connectivity). The connectivity and weights of hidden [neurons](https://en.wikipedia.org/wiki/Artificial_neuron "Artificial neuron") are fixed and randomly assigned. The weights of output neurons can be learned so that the network can (re)produce specific temporal patterns. (Source: [WIkipedia](https://en.wikipedia.org/wiki/Echo_state_network))

Open `Echo_State_Network.ipynb` in `model/nb` and follow the instructions to run the model.
## Results
### RNN model
|Feature Set|Precision                        |Recall |Accuracy                        |
|----------------|-------------------------------|-----------------------------|-------|
|first|1           |2          |3
|second          |4      |5          |6
|third          |7      |8          |9

### ESN model
In the `Echo_State_Network.ipynb` notebook, we tried several different combinations of the parameters. Using the scaled Bitcoin price data, an optimal set of `reservoir = 500`, `sparsity = 0.2`, `radius = 1.5`, and `noise = 0.001` gives the MSE around `0.1547`.

## Future Steps
### More Data Scraping  
Our time limitations posed the greatest constraint, as the most crucial part of this idea is to get as much relevant data related to cryptocurrency and Bitcoin as possible. This is needed for our model to be trained on a holistic and realistic depiction of what posts, articles, etc. people are reacting to in order to accurately gauge public sentiment. If we had more time and perhaps more people, we could perform a wider and deeper search for this data to improve our model.  
### Financial Sentiment Analyzer
We attempted to search for a better sentiment analyzer since TextBlob’s performance was less than ideal. We wanted to find one that specifically dealt with financial text, but were unable to find such a tool. This is probably because an actual robust financial text sentiment analyzer would likely be privatized by FinTech organizations due to its potentially powerful capabilities. Going forward, an additional component of this project could be training our own financial text sentiment analyzer and furthering the open source agenda of our application. 

## Authors
* **[Anthony Burre](https://www.linkedin.com/in/anthony-burre-ab44a1123/)**
* **[Courtney Luk](https://www.linkedin.com/in/courtneyluk/)**
* **[Lu Yu](https://www.linkedin.com/in/yu24l/)**
* **[Max Matuska](https://www.linkedin.com/in/max-matuska-4b736014a/)**

## Acknowledgments

* We would like to express our gratitude to the AMLI instructor team that provided so much help and support on this project, as well as Sidnie and Liza who organized this great opportunity.

## References
* [Predicting Stock Prices with Echo State Networks](https://towardsdatascience.com/predicting-stock-prices-with-echo-state-networks-f910809d23d4)
* [Predicting Cryptocurrency Prices with Machine Learning](https://medium.com/datadriveninvestor/predicting-cryptocurrency-prices-with-machine-learning-1b5a711d3937)
* [How Cryptocurrency Prices Work, Explained](https://cointelegraph.com/explained/how-cryptocurrency-prices-work-explained)
