# moddata

![Flake8 Lint Check](https://github.com/wegar-2/moddata/actions/workflows/ruff-lint.yml/badge.svg)
![CI](https://github.com/wegar-2/moddata/actions/workflows/python-tests.yml/badge.svg)
![codecov](https://codecov.io/gh/wegar-2/moddata/branch/main/graph/badge.svg)


Provides data for use in modeling.

## 1. Installation

To install this package run:
```
pip install git+https://github.com/wegar-2/moddata.git@main
```

## 2. API
Interface contains functions: 
* `load_data` - loads predefined datasets
* `make_milisec_data` - allows for generating 1 day of 
data on prices with predefined quotes arrival intensity

### 2.1. `load_data`
a single parameter - name of the dataset to load.

List of currently available datasets:
1. `bankchurn` - [this](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset) Kaggle dataset
2. `btc` - bitcoin price data in USD for years 2017-2021, based on [this Kaggle dataset](https://www.kaggle.com/datasets/prasoonkottarathil/btcinusd?resource=download)
3. `pl_banking_stocks` - daily prices of stocks of select 
Polish banks for period 2005-01-01 through 2024-12-31 
(data source: [stooq.com](https://stooq.com/))
4. `sunspots` - daily total sunspot number data as per [SILSO](https://www.sidc.be/SILSO/datafiles)
5. `geomagnetic_activity` - data on geomagnetic activity as per [GFZ Centre for Geosciences](https://kp.gfz.de/en/data) 
6. `world_bank_oil_gold_monthly_prices.parquet` - data on oil prices
(average, Brent, Dubai) and gold price from 
[World Bank's Commodity Markets](https://www.worldbank.org/en/research/commodity-markets)

### 2.2. `make_milisec_data`




## 3. Linting and Running Unit Tests

Run unit tests from the main package directory with:
```
pytest
```

Run `ruff` check with:
```commandline
uv run ruff check
```

Check tests coverage with:
```
pytest --cov=moddata tests/
```