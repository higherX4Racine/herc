#  Copyright (c) 2022 by Higher Expectations for Racine County.

import pytest

from herc.bls import laus


@pytest.fixture(scope='module',
                params=range(3, 10))
def measure(request):
    r"""One element from the `laus.Measure` enum."""

    return laus.Measure(request.param)


def test_series_id_creation(measure,
                            racine_geo):
    r"""combine different geos with different measures"""

    assert laus.series_id(racine_geo, measure) == 'LAU' + racine_geo + '0' + str(int(measure))
