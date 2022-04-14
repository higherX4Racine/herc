#  Copyright (c) 2022 by Higher Expectations for Racine County.
r"""Internal constants for dealing with Local Area Unemployment Statistics"""

from pandas.api.types import CategoricalDtype

URL = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'

JSON_CONTENT_TYPE = {
    'Content-type': 'application/json'
}

OUTPUT_COLUMNS = {
    'series': 'Series',
    'year': 'Year',
    'periodName': 'Month',
    'value': 'Value'
}

MONTHS = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

OUTPUT_DTYPES = {
    'Series': 'str',
    'Year': 'int32',
    'Month': CategoricalDtype(categories=MONTHS,
                              ordered=True),
    'Value': 'float32'
}

