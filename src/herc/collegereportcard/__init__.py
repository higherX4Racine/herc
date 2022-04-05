#  Copyright (c) 2022 by Higher Expectations for Racine County.
r"""Access data from https://api.data.gov/ed/collegescorecard/v1/schools

    This is a huge database based on IPEDS that has a nice JSON API.

"""
from .url import url

__all__ = [
    'url',
]