import pandas as pd

from moddata.extractor.cboe_vix_data_extractor import CboeVIXDataExtractor


def test_cboe_vix_data_extractor():
    data = CboeVIXDataExtractor().extract()
    assert isinstance(data, pd.DataFrame)
    assert all(data.columns == pd.MultiIndex.from_product([
        ["VIX"], ["open", "high", "low", "close"]]))
