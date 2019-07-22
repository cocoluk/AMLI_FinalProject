import time
from selenium import webdriver

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

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", '/Users/luyu/Desktop/btc_data')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

driver = webdriver.Firefox(firefox_profile=profile)


for i in range(len(page)):
    driver.get(url+page[i])
    time.sleep(2)
    driver.find_element_by_id("sidebar-tools-btn").click()
    time.sleep(2)
    driver.find_element_by_id("data-download").click()
    time.sleep(3)



# TODO: UPLOAD THE SAVED FILE ON DROPBOX???

driver.quit()