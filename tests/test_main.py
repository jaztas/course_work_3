import pytest
from main import miss_empty_dict, get_executed, sorted_operations, five_last_operations, data


def test_miss_empty_dict():
	result = miss_empty_dict()
	assert len(result) == 90


def test_get_executed():
	result = get_executed()
	assert len(result) == 76


def test_sorted_operations():
	result = sorted_operations()
	assert len(result) == 76
	assert result[0]['date'] == '2019-12-07T06:17:14.634890'


def test_five_last_operations():
	result = five_last_operations(data)
	assert len(result) == 5
