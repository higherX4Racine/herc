#  Copyright (c) 2022 by Higher Expectations for Racine County.

import datetime
import json
import os
from typing import (
    Collection,
    List,
)

import requests

from .constants import (
    URL,
    JSON_CONTENT_TYPE,
)


def get(series: Collection[str],
        start_year: int,
        final_year: int = None,
        api_key: str = None) -> List[requests.Response]:
    r"""Get data from the College Scorecard API.

    The call will filter by ``ids`` and ``year`` (using `latest` as the
    default year), and query for each of ``fields``.

    Parameters
    ----------
    series : Collection[str]
        LAUS series values.
    start_year : int
        The earliest year to get data for.
    final_year : int, optional
        The latest year to get data for.
    api_key: str, optional
        The user's API_KEY for College Scorecard. Defaults to API_BLS_GOV_KEY.

    Returns
    -------
    List[requests.Response]
        The response(s) to the request from the API server.

    """

    if api_key is None:
        api_key = os.environ['API_BLS_GOV_KEY']

    if final_year is None:
        final_year = datetime.datetime.now().year

    if final_year - start_year > 19:
        result = [get(series,
                      year,
                      min(year + 19, final_year),
                      api_key)[0] for
                  year in range(start_year, final_year, 20)]
    else:
        result = [
            requests.post(URL,
                          data=json.dumps({'seriesid': series,
                                           'startyear': str(start_year),
                                           'endyear': str(final_year),
                                           'registrationkey': api_key}),
                          headers=JSON_CONTENT_TYPE),
        ]

    return result
