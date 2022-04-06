#  Copyright (c) 2022 by Higher Expectations for Racine County.
r"""Values that won't change much between runs."""

URL = r'https://api.data.gov/ed/collegescorecard/v1/schools'
r"""The address of the College Scorecard API"""


FIELDS = [
    "school.name",
    "id",
    "ope6_id",
    "latest.student.size",
    "latest.student.enrollment.undergrad_12_month",
    "latest.completion.completion_rate_4yr_150nt",
    "latest.completion.completion_rate_less_than_4yr_150nt",
]
r"""The FIELDS constant is a list of column names to query for.

    These are dot-separated strings that include both the "dev-category" for a
    field and its "developer-friendly" name.

"""


HERA_UNIT_IDS = [
    238193,
    45175001,
    45175002,
    451750,
    238430,
    238458,
    238476,
    238616,
    238759,
    459851,
    459842,
    239105,
    239248,
    239309,
    239318,
    239390,
    240453,
    491288,
    240374,
    491297,
    240189,
    240125,
    240338
]
r"""The HERA_UNIT_IDS constant is a list of integer IDs for HERA schools.

    HERA is the Higher Education Regional Alliance of Southestern Wisconsin.

"""
