#  Copyright (c) 2022 by Higher Expectations for Racine County.
r"""Tools for accessing LAUS data from the BLS Labor Statistics API"""

from enum import IntEnum
import json
import os
from typing import Collection

import requests


class Measure(IntEnum):
    r"""There are seven measures in the LAUS data."""
    UNEMPLOYMENT_RATE = 3
    UNEMPLOYMENT = 4
    EMPLOYMENT = 5
    LABOR_FORCE = 6
    EMPLOYMENT_POPULATION_RATIO = 7
    LABOR_FORCE_PARTICIPATION_RATE = 8
    CIVILIAN_NONINSTITUTIONAL_POPULATION = 9


def series_id(geography: str,
                   measure: Measure) -> str:
    r"""Create an ID for a series of LAUS data for a specific geography.

    Parameters
    ----------
    geography : str
        A 14-character geographic id. See `herc.GeographicAreaType`.
    measure : Measure
        One of the seven possible LAUS measures.

    Returns
    -------
    str
        An 18-character string in LAGGGGGGGGGGGGGGMM format.

    """

    return f'LAU{geography}{measure:0>2}'


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

    return requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/',
                         data=json.dumps({'seriesid': series,
                                          'startyear': str(start_year),
                                          'endyear': str(end_year),
                                          'registrationkey': api_key}),
                         headers={'Content-type': 'application/json'})
