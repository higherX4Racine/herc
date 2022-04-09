#  Copyright (c) 2022 by Higher Expectations for Racine County.
r"""Internal constants for dealing with Local Area Unemployment Statistics"""

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


