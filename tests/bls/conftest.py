#  Copyright (c) 2022 by Higher Expectations for Racine County.

import pytest


@pytest.fixture(scope="package",
                params=[
                    'ST5500000000000',
                    'MT5539540000000',
                    'CA5537600000000',
                    'CN5510100000000',
                    'CT5566000000000',
                ])
def racine_geo(request):
    r"""A geo id related to Racine, WI"""
    return request.param
