# moddata

Provides data for use in modeling.

Interface consists of a single function ```load_data```. It accepts 
a single parameter - name of the dataset to load.

List of currently available datasets:
1. `bankchurn` - [this](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset) Kaggle dataset
2. `btc` - bitcoin price data in USD for years 2017-2021, based on [this Kaggle dataset](https://www.kaggle.com/datasets/prasoonkottarathil/btcinusd?resource=download)
3. `pl_banking_stocks` - daily prices of stocks of select 
Polish banks for period 2005-01-01 through 2024-12-31 
(data source: [stooq.com](https://stooq.com/))
4. 

To install this package run:
```
pip install git+https://github.com/wegar-2/moddata.git@main
```