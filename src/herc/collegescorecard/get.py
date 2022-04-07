#  Copyright (c) 2022 by Higher Expectations for Racine County.
r"""make a call to the College Scorecard API"""

import os
from typing import (
    Collection,
)

import requests

from .field import Field
from .constants import URL


def get(ids: Collection[int],
        fields: Collection[Field],
        year: int = None,
        api_key: str = None) -> requests.Response:
    r"""Get data from the College Scorecard API.

    The call will filter by ``ids`` and ``year`` (using `latest` as the
    default year), and query for each of ``fields``.

    Parameters
    ----------
    ids : Collection[int]
        UNIT_ID values for the campuses of interest.
    fields : Collection[Field]
        category and name values for each column of data
    year : int, optional
        The year to get data for. Defaults to 'latest'.
    api_key: str, optional
        The user's API_KEY for College Scorecard. Defaults to API_DATA_GOV_KEY.

    Returns
    -------
    requests.Response
        The response to the request from the API server.

    """

    if api_key is None:
        api_key = os.environ['API_DATA_GOV_KEY']

    params = {
        'id': ','.join(map(str, ids)),
        'fields': ','.join(map(lambda f: f.render_as_parameter(year),
                               fields)),
        'per_page': len(ids),
        'api_key': api_key,
    }

    return requests.get(URL, params=params)
