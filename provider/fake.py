# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Provider for Faker which adds fake product names."""

from faker.providers import BaseProvider

CATEGORIES = [
    'smartphones',
    'laptops',
]


class FakeProduct(BaseProvider):
    """Provider for Faker which adds fake product names."""

    def category(self):
        return self.random_element(CATEGORIES)
