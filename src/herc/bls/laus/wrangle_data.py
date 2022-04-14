#  Copyright (c) 2022 by Higher Expectations for Racine County.

from typing import (
    Iterable,
    List,
)

import pandas
import requests

from .constants import OUTPUT_COLUMNS


def _consolidate(d):
    df = pandas.DataFrame(d['data'])
    df.insert(0, 'series', d['seriesID'])
    return df


def _extract_data_payload(response: requests.Response) -> Iterable:
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

    tables = [pandas.concat(map(_consolidate,
                                _extract_data_payload(r)))
              for r in responses]

    return pandas.concat(tables)[OUTPUT_COLUMNS.keys()].\
        convert_dtypes().\
        rename(columns=OUTPUT_COLUMNS)
