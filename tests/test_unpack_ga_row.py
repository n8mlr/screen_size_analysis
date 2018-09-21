#!/usr/bin/env python3
import screen_size_analysis as sa

def test_unpack_row_flatten_counts():
	result = sa.unpack_row('1080x810,2')
	assert len(result) == 2

def test_unpack_row_expected_outputs():
	result = sa.unpack_row('2080x1800,desktop,3')
	assert len(result) == 3
	assert result[0][0] == 2080
	assert result[0][1] == 1800
	assert result[0][2] == 2080 * 1800
	assert result[0][3] == 2080 / 1800
	assert result[0][4] == 'desktop'

def test_unpack_row_ignore_entries_missing_dimensions():
	result = sa.unpack_row('(not set),desktop,4')
	assert result == None