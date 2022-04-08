#  Copyright (c) 2022 by Higher Expectations for Racine County.

from herc.collegescorecard.constants import (
    URL,
    FIELDS,
    HERA_UNIT_IDS
)


def test_url():
    assert not isinstance(URL,
                          list)
    assert isinstance(URL,
                      str)


def test_fields():
    assert isinstance(FIELDS,
                      list)
    assert len(FIELDS) == 7


def test_hera_ids():
    assert isinstance(HERA_UNIT_IDS,
                      list)
    assert len(HERA_UNIT_IDS) == 21
