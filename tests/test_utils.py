# This file is part of the Provider API Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Module for Utils testing."""

import pytest

from provider.utils import strtobool


@pytest.mark.parametrize(
    'value',
    ('y', 'Y', 'yes', 't', 'True', 'ON', 1,))
def test_should_return_true(value):
    assert strtobool(value) is True


@pytest.mark.parametrize(
    'value',
    ('n', 'N', 'no', 'f', 'False', 'OFF', 0))
def test_should_return_false(value):
    assert strtobool(value) is False


def test_should_raise_value_error():
    with pytest.raises(ValueError):
        strtobool('FOO_BAR')
