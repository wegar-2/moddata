from pathlib import Path

import pandas as pd


class OilGoldMonthlyPricesPipeline:
    """
    Prepares Python dataset of nominal monthly prices of commodities.
    Monthly data for years: 1960-2025 (both inclusive).
    All prices - nominal!!!
    Data source - World Bank:
    https://www.worldbank.org/en/research/commodity-markets
    (1) oil - average, price per barrel in USD; average spot price of: Brent,
    Dubai and West Texas  Intermediate, equally weighed;
    Sources: World Bank
    (2) oil - Brent, price per barrel in USD; Crude oil, UK Brent 38` API.
    Sources: Bloomberg; Energy Intelligence Group (EIG);
    Organization of Petroleum Exporting Countries (OPEC); World Bank.
    (3) oil - Dubai, price per barrel in USD;
    Crude oil, Dubai Fateh 32` API for years 1985-present;
    1960-84 refer to Saudi Arabian Light, 34` API.
    Sources: Bloomberg; Energy Intelligence Group (EIG);
    Organization of Petroleum Exporting Countries (OPEC); World Bank.
    (4) gold - price per troy ounce in USD; spot average of daily rates,
    from June 2025; previously (UK), 99.5% fine, London afternoon fixing,
    average of daily rates
    Sources: Bloomberg; Kitco.com; International Monetary Fund,
    International Financial Statistics;
    London Bullion Market; Metals Week; Platts Metals Week;
    Shearson Lehman Brothers, Metal Market Weekly Review;
    Thomson Reuters Datastream; World Bank.
    """

    def run(self):
        data = pd.read_csv(
            str(
                Path(__file__).parent.parent / "data" /
                "world_bank_oil_gold_monthly_prices.csv"
            ),
            sep=";", decimal=","
        )
        data["yearmon"] = pd.to_datetime(data["yearmon"], format="%YM%m")
        data.to_parquet(
            str(
                Path(__file__).parent.parent / "data" /
                "world_bank_oil_gold_monthly_prices.parquet"
            )
        )
