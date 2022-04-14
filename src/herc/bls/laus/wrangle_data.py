#  Copyright (c) 2022 by Higher Expectations for Racine County.

from typing import (
    Iterable,
    List,
)

import pandas
import requests

from .constants import (
    OUTPUT_COLUMNS,
    OUTPUT_DTYPES,
)


def _wrangle_series(extract):
    df = pandas.DataFrame(extract['data'])
    df.insert(0, 'series', extract['seriesID'])
    return df[OUTPUT_COLUMNS.keys()]


def _extract_series(response: requests.Response) -> Iterable:
    return filter(lambda x: bool(x['data']),
                  response.json()['Results']['series'])


def wrangle(responses: List[requests.Response]) -> pandas.DataFrame:
    r"""Do the absolute minimum necessary to make a response into table

    Parameters
    ----------
    responses : List[requests.Response]
        the result of calling `get`.

    Returns
    -------
    pandas.DataFrame
        A table with four columns: Series, Year, Month, and Value.

    """

    tables = [pandas.concat(map(_wrangle_series,
                                _extract_series(response)))
              for response in responses]

    return pandas.concat(tables).\
        rename(columns=OUTPUT_COLUMNS).\
        astype(OUTPUT_DTYPES)
