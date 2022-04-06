#  Copyright (c) 2022 by Higher Expectations for Racine County.
r"""A data field from the College Scorecard API needs some context to work."""


class Field:
    r"""One column of data from the College Scorecard API

    As per https://collegescorecard.ed.gov/data/documentation, some fields
    have special characteristics:

        The year may be any year of data available (example: 2012), or use the
        word "latest" to get the most recent data available from the API. Using
        the "latest" key will allow your application to access the new data as
        soon as it is released.

        - The "school" category has no year.
        - "id", "ope6_id", "ope8_id" and "location" have no category or year.

    Parameters
    ----------
    name : str
        The 'developer-friendly-name' of the variable.
    category : str, optional
        The 'dev-category' the variable belongs to. Defaults to 'root'.

    Notes
    -----
    A to-do: create a class/dictionary for validating field names and
    categories.

    """

    def __init__(self, name: str, category: str = None):
        self._name = name
        if category is None:
            category = 'root'
        if category == 'root' and name not in self.root_fields():
            raise ValueError('"%s" is not part of the "root" category!'
                             % name)
        self._category = category

    @staticmethod
    def root_fields() -> list:
        r"""The developer-friendly names of fields in the 'root' category."""
        return ['id', 'ope6_id', 'ope8_id', 'location']

    @staticmethod
    def no_year_categories() -> list:
        r"""Members of these categories have no year when rendered."""
        return [None, 'root', 'school']

    @property
    def name(self) -> str:
        r"""The developer-friendly-name of the field."""

        return self._name

    @property
    def category(self) -> str:
        r"""The dev-category that the field belongs to."""
        return self._category

    @property
    def uses_year(self) -> bool:
        r"""Some names and categories must not be rendered with a year."""
        return self._category not in self.no_year_categories()

    def render_as_parameter(self, year: int = None) -> str:
        r"""Render the field as a string that the API can consume

        Parameters
        ----------
        year : int, optional
            The year from whence the datum should come, defaults to 'latest'.

        Returns
        -------
        str : a dot-separated key path: year.category.name

        """

        if year is None:
            year = 'latest'

        return '.'.join(filter(None, [
            str(year) if self.uses_year else None,
            None if self.category == 'root' else self.category,
            self.name
        ]))
