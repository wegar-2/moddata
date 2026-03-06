from datetime import date, datetime, time, timedelta

import numpy as np
import pandas as pd

from moddata.src.constants import MICRO_SECS_PER_DAY


def make_milisec_data(
        inter_arrival_time_milisecs: float = 50,
        start_value: float = 5.00,
        daily_sigma: float = 0.02,
        day: date = date(2021, 1, 1),
        seed: int = 123_456
):
    """
    Generate 1 day of data using GBM without drift.
    Arrivals have exponential distribution.

    :param inter_arrival_time_milisecs:
    :param start_value: starting value of the GBM process
    :param daily_sigma: standard deviation of the GBM for 1d period
    :param day: date to use in the simulation
    :param seed: random seed
    :return: pd.DataFrame with columns quote_time and price
    """
    dt: datetime = datetime.combine(day, time(0, 0, 0, 0))
    time_grid: list[datetime] = [dt]
    prices: list[float] = [start_value]
    np.random.seed(seed)

    while dt.date() == day:
        time_diff = int(np.random.exponential(
            scale=inter_arrival_time_milisecs)) + 1
        dt += timedelta(milliseconds=time_diff)
        time_grid.append(dt)
        prices.append(
            prices[-1] * (
                    1 +
                    np.random.standard_normal(size=1)[0] *
                    np.sqrt(time_diff / MICRO_SECS_PER_DAY) *
                    daily_sigma
            )
        )

    return pd.DataFrame(data={"quote_time": time_grid, "price": prices})
