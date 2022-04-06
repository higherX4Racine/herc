#  Copyright (c) 2022 by Higher Expectations for Racine County.
r"""make sure that fields behave appropriately"""

import pytest

from herc.collegescorecard import Field


def test_vanilla_field_init():
    r"""Boring old initialization should just work."""
    field = Field('hello', 'world')
    assert field.name == 'hello'
    assert field.category == 'world'



def test_raising_field_init():
    r"""A non-root field in the 'root' category should raise a ValueError."""
    with pytest.raises(ValueError) as exception_info:
        Field(name='foo')

    assert str(exception_info.value) == \
           '"foo" is not part of the "root" category!'


@pytest.mark.parametrize('name,category,year,should_be', [
    ['foo', 'bar', 1999, '1999.bar.foo'],
    ['foo', 'bar', None, 'latest.bar.foo'],
    ['id', None, 1999, 'id'],
    ['name', 'school', None, 'school.name']
])
def test_field_rendering(name, category, year, should_be):
    r"""The rendered keypath should only include allowed components."""
    field = Field(name, category)
    assert field.render_as_parameter(year) == should_be

