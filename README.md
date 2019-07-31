
# AMLI Project - Bitcoin Price Prediction

 > This is a final project from Google Applied Machine Learning Intensive (AMLI) in summer 2019. 

 > Using machine learning (ML) techniques and given the Bitcoin historical data and sentiment analysis of relevant Reddit and Twitter posts, the model could predict the trend and the exact price of Bitcoin.

 > Keywords: applied machine learning, Bitcoin, cryptocurrency, price prediction, RNN, sentiment analysis

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)

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
```
GetOldTweets3 --querysearch "europe refugees" --maxtweets 10
```

Example 2 - Get the last 10 top tweets by username:
```
GetOldTweets3 --username "barackobama" --toptweets --maxtweets 10
```

Example 3 - Get tweets by the username and bound dates (until date is not included):
```
GetOldTweets3 --username "barackobama" --since 2015-09-10 --until 2015-09-12 --maxtweets 10
```

Example 4 - Get tweets by several usernames:
```
GetOldTweets3 --username "BarackObama,AngelaMerkeICDU" --usernames-from-file userlist.txt --maxtweets 10
```

Example 5 - Get tweets by language:
```
GetOldTweets3 --querysearch "bitcoin" --lang cn --maxtweets 10
```
See [GetOldTweets3](https://pypi.org/project/GetOldTweets3/) for additional Twitter criteria.

### Reddit
### Sentiment Analysis

## Model
## Results
## Future Directions


## Authors
* **Anthony Burre**  - [LinkedIn](https://www.instagram.com/anthonyburre/)
* **Courtney Luk**  - [LinkedIn](https://www.linkedin.com/in/courtneyluk/)
* **Lu Yu**  - [LinkedIn](https://www.linkedin.com/in/yu24l/)
* **Max Matuska**  - [LinkedIn](https://www.linkedin.com/in/max-matuska-4b736014a/)

## Acknowledgments

* Thank 
* 
## References
*
*