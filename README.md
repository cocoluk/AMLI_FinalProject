
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
### Reddit
### Sentiment Analysis

## Model
## Results
## Future Directions


## Authors
* **Anthony Burre**  - [LinkedIn](https://www.instagram.com/anthonyburre/)
* **Courtney**  - [LinkedIn](https://www.linkedin.com/in/courtneyluk/)
* **Lu Yu**  - [LinkedIn](https://www.linkedin.com/in/yu24l/)
* **Max Matuska**  - [LinkedIn](https://www.linkedin.com/in/max-matuska-4b736014a/)

## Acknowledgments

* Thank 
* 
## References
*
*