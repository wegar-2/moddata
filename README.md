# moddata

![CI](https://github.com/wegar-2/moddata/actions/workflows/python-tests.yml/badge.svg)
![codecov](https://codecov.io/gh/wegar-2/moddata/branch/main/graph/badge.svg)
![Flake8 Lint Check](https://github.com/wegar-2/moddata/actions/workflows/flake8-lint.yml/badge.svg)
![Pylint Check](https://github.com/wegar-2/moddata/actions/workflows/pylint.yml/badge.svg)


Provides data for use in modeling.

Interface consists of a single function ```load_data```. It accepts 
a single parameter - name of the dataset to load.

List of currently available datasets:
1. `bankchurn` - [this](https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset) Kaggle dataset
2. `btc` - bitcoin price data in USD for years 2017-2021, based on [this Kaggle dataset](https://www.kaggle.com/datasets/prasoonkottarathil/btcinusd?resource=download)
3. `pl_banking_stocks` - daily prices of stocks of select 
Polish banks for period 2005-01-01 through 2024-12-31 
(data source: [stooq.com](https://stooq.com/))
4. `sunspots` - daily total sunspot number data as per [SILSO](https://www.sidc.be/SILSO/datafiles)
5. `geomagnetic_activity` - data on geomagnetic activity as per [GFZ Centre for Geosciences](https://kp.gfz.de/en/data) 


To install this package run:
```
pip install git+https://github.com/wegar-2/moddata.git@main
```

Run unit tests from the main package directory with:
```
pytest
```

Check tests coverage with:
```
pytest --cov=moddata tests/
```