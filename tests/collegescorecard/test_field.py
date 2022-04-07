#  Copyright (c) 2022 by Higher Expectations for Racine County.
r"""make sure that fields behave appropriately"""

import pytest

from herc.collegescorecard import Field


@pytest.fixture(scope='module')
def field_name() -> str:
    r"""a reusable field name."""
    return 'bar'


@pytest.fixture(scope='module')
def field_category() -> str:
    r"""A reusable field category"""
    return 'foo'


@pytest.fixture(scope='function')
def field(field_name, field_category) -> Field:
    return Field(field_name, field_category)


def test_vanilla_field_init(field_name,
                            field_category,
                            field):
    r"""Boring old initialization should just work."""
    assert field.name == field_name
    assert field.category == field_category
    another = Field(field_name, field_category)
    assert another == field


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


def test_field_to_str(field):
    r"""The `__str__` operator should equal default rendering."""

    assert str(field) == field.render_as_parameter()


def test_field_to_repr(field_name,
                       field_category,
                       field):
    r"""The `__repr__` operator should make a callable item."""

    should_be = f'Field(name=\'{field_name}\', category=\'{field_category}\')'
    assert repr(field) == should_be
    assert eval(should_be) == field