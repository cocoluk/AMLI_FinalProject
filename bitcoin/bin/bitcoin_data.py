import time
from selenium import webdriver

# This Python script is to automate the web browser and 
# download the 39 csv files from https://charts.bitcoin.com/btc/chart/
# to save more time.

# author: Lu Yu
# version: 07/30/19

# set the link and the desired features to be fetched
url = "https://charts.bitcoin.com/btc/chart/"
page = ["price", "market-cap", "money-supply", "chain-value-density",
        "price-volatility", "daily-transactions", "transaction-value", "total-transactions",
        "fee-percentage", "fee-rate", "transaction-amount", "utxo-amount",
        "utxo-value", "block-size", "block-interval", "blockchain-size",
        "block-height", "blocks-daily", "transactions-per-block", "hash-rate",
        "difficulty", "transaction-fees", "transaction-fees-value", "miner-revenue",
        "miner-revenue-value", "hash-rate-growth-14d", "quarterly-hash-rate-growth", "annual-hash-rate-growth",
        "inflation", "metcalfe-utxo", "metcalfe-tx", "velocity",
        "velocity-quarter", "velocity-daily", "transaction-size", "output-volume",
        "output-value", "utxo-set-size", "utxo-growth"]

# initiate the web browser
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)

# The file will be saved to a fold called bitcoin on the Desktop
# NOTICE: may need to change the file path using different computers
profile.set_preference("browser.download.dir", '../data/bitcoin_data')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

driver = webdriver.Firefox(firefox_profile=profile)

# walk through each page
for i in range(len(page)):
    driver.get(url+page[i])
    time.sleep(2)
    driver.find_element_by_id("sidebar-tools-btn").click() # click sidebar
    time.sleep(2)
    driver.find_element_by_id("data-download").click() # click download
    time.sleep(3)

driver.quit()