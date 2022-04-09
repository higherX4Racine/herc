#  Copyright (c) 2022 by Higher Expectations for Racine County.
r"""In LAUS data, a series is a combination of a place and a measure."""

from typing import Tuple

from . import Measure


def series_id(geography: str,
              measure: Measure) -> str:
    r"""Create an ID for a series of LAUS data for a specific geography.

    Parameters
    ----------
    geography : str
        A 15-character geographic id. See `herc.GeographicAreaType`.
    measure : Measure
        One of the seven possible LAUS measures.

    Returns
    -------
    str
        An 18-character string in LAUGGGGGGGGGGGGGGMM format.

    """

    return f'LAU{geography}{measure:0>2}'


def split_id(laus_id: str) -> Tuple[str, Measure]:
    r"""Break up a LAUS series ID into its component geography and measure.

    Parameters
    ----------
    laus_id : str
        The 20-digit ID, including the beginning "LAU"

    Returns
    -------
    geo_id : str
        a FIPS-like geographic ID like you'd get from `herc.bls`
    measure : Measure
        the enum value for the specific statistic in this series.

    """

    return (
        laus_id[3:18],
        Measure(int(laus_id[-2:]))
    )
