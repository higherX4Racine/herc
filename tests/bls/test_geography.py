#  Copyright (c) 2022 by Higher Expectations for Racine County.

import pytest

from herc.bls.geography import GeographicAreaType
from herc.bls import AREA_TYPES


@pytest.mark.parametrize('area_type', AREA_TYPES.values())
def test_area_type_creation(area_type):
    r"""A newly-created type should be identical to its progenitor."""

    new_type = GeographicAreaType(str(area_type),
                                  area_type.prefix,
                                  area_type.digits)

    assert new_type.label == area_type.label
    assert new_type.prefix == area_type.prefix
    assert new_type.digits == area_type.digits


def test_geo_id_for(racine_geo):
    r"""do the area_type instances perform correctly for Racine places?"""

    prefix = racine_geo[:2]
    containing_fips = int(racine_geo[2:4])
    code = racine_geo[4:].strip('0')
    if code:
        code = int(code)
    else:
        code = 0
    if prefix == 'CT':
        code *= 1000
    actually_is = AREA_TYPES[prefix].id_for(containing_fips, code)
    assert actually_is == racine_geo


def test_geo_area_type_repr():
    r"""One string check because BORING"""

    assert repr(AREA_TYPES['DV']) == "GeographicAreaType('Metropolitan divisions', 'DV', 5)"
