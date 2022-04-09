#  Copyright (c) 2022 by Higher Expectations for Racine County.

import json
import os
from typing import Collection

import requests

from .constants import (
    URL,
    JSON_CONTENT_TYPE,
)
def get(series: Collection[str],
        start_year: int,
        end_year: int,
        api_key: str = None) -> requests.Response:
    r"""Get data from the College Scorecard API.

    The call will filter by ``ids`` and ``year`` (using `latest` as the
    default year), and query for each of ``fields``.

    Parameters
    ----------
    series : Collection[str]
        LAUS series values.
    start_year : int
        The earliest year to get data for.
    end_year : int
        The latest year to get data for.
    api_key: str, optional
        The user's API_KEY for College Scorecard. Defaults to API_BLS_GOV_KEY.

    Returns
    -------
    requests.Response
        The response to the request from the API server.

    """

    if api_key is None:
        api_key = os.environ['API_BLS_GOV_KEY']

    return requests.post(URL,
                         data=json.dumps({'seriesid': series,
                                          'startyear': str(start_year),
                                          'endyear': str(end_year),
                                          'registrationkey': api_key}),
                         headers=JSON_CONTENT_TYPE)
