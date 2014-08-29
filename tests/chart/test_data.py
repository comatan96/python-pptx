# encoding: utf-8

"""
Test suite for pptx.chart.data module
"""

from __future__ import absolute_import, print_function

import pytest


from pptx.chart.data import ChartData


class DescribeChartData(object):

    def it_knows_its_current_categories(self, categories_get_fixture):
        chart_data, expected_value = categories_get_fixture
        assert chart_data.categories == expected_value

    # fixtures -------------------------------------------------------

    @pytest.fixture
    def categories_get_fixture(self, categories):
        chart_data = ChartData()
        chart_data._categories = list(categories)
        expected_value = categories
        return chart_data, expected_value

    # fixture components ---------------------------------------------

    @pytest.fixture
    def categories(self):
        return ('Foo', 'Bar', 'Baz')