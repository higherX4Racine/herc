#  Copyright (c) 2022 by Higher Expectations for Racine County.
r"""I think it makes sense to keep track of the stats in an enum."""

from enum import IntEnum


class Measure(IntEnum):
    r"""There are seven measures in the LAUS data."""
    UNEMPLOYMENT_RATE = 3
    UNEMPLOYMENT = 4
    EMPLOYMENT = 5
    LABOR_FORCE = 6
    EMPLOYMENT_POPULATION_RATIO = 7
    LABOR_FORCE_PARTICIPATION_RATE = 8
    CIVILIAN_NONINSTITUTIONAL_POPULATION = 9
