#  Copyright (c) 2022 by Higher Expectations for Racine County.
r"""Utilities for dealing with geographic ids.

You can get a full list of each geographical area at
https://download.bls.gov/pub/time.series/la/la.area

"""


class GeographicAreaType:
    r"""BLS uses their own version of the old FIPS for tracking locations.

    Parameters
    ----------
    label : str
        A human-readable description of the area type
    prefix : str
        The two-letter string that is prepended to a series ID
    digits : int, optional
        The number of digits the type needs. Default is 0

    """

    def __init__(self, label: str, prefix: str, digits: int = None):
        if len(prefix) != 2:
            raise ValueError('the prefix must be a two-character string.')
        self._prefix = prefix
        self._label = label
        self._digits = 0 if digits is None else digits

    def id_for(self, containing_fips: int, code: int = None) -> str:
        r"""Create the 15-digit geo code for the BLS to use in a series ID

        Parameters
        ----------
        containing_fips : int
            the FIPS code of the containing state or region
        code : int
            the FIPS-like code of the internal region.

        """

        if 0 > containing_fips >= 100:
            raise ValueError('the containing fips must be a two-digit number.')

        if code is None or self._digits == 0:
            code = 0

        suffix = f'{code:0>{self._digits}}'
        return f'{self._prefix}{containing_fips:0>2}{suffix:0<11}'

    @property
    def label(self):
        return self._label

    @property
    def digits(self):
        return self._digits

    @property
    def prefix(self):
        return self._prefix

    def __str__(self):
        return self.label

    def __repr__(self):
        return f"GeographicAreaType('{self.label}', '{self.prefix}', {self.digits})"


AREA_TYPES = {
    'ST': GeographicAreaType(prefix='ST', digits=0, label='Statewide'),
    'MT': GeographicAreaType(prefix='MT', digits=4, label='Metropolitan areas'),
    'DV': GeographicAreaType(prefix='DV', digits=5, label='Metropolitan divisions'),
    'MC': GeographicAreaType(prefix='MC', digits=4, label='Micropolitan areas'),
    'CA': GeographicAreaType(prefix='CA', digits=3, label='Combined areas'),
    'CN': GeographicAreaType(prefix='CN', digits=3, label='Counties and equivalents'),
    'CS': GeographicAreaType(prefix='CS', digits=5, label='"Cities and towns above 25,000 population"'),
    'CT': GeographicAreaType(prefix='CT', digits=5, label='"Cities and towns above 25,000 population"'),
    'PT': GeographicAreaType(prefix='PT', digits=8, label='Parts of cities that cross county boundaries'),
    'SA': GeographicAreaType(prefix='SA', digits=4, label='Multi - entity small labor market areas'),
    'ID': GeographicAreaType(prefix='ID', digits=5, label='Intrastate parts of interstate areas'),
    'IM': GeographicAreaType(prefix='IM', digits=4, label='Intrastate parts of interstate areas'),
    'IS': GeographicAreaType(prefix='IS', digits=4, label='Intrastate parts of interstate areas'),
    'BS': GeographicAreaType(prefix='BS', digits=0, label='Balance of state areas'),
    'RD': GeographicAreaType(prefix='RD', digits=0, label='Census regions'),
}
