#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pywc
----------------------------------

Tests for `pywc` module.
"""

import pytest
from pywc import pywc

@pytest.fixture
def file_string():
    "Return a string of file contents read in rb mode"
    filename = 'tests/ch.txt'
    with open(filename, 'rb') as fin:
        filestring = fin.read()

    return filestring

def test_count_lines(file_string):
    assert pywc.count_lines(file_string) == 3

def test_count_words(file_string):
    assert pywc.count_words(file_string) == 4

def test_count_bytes(file_string):
    assert pywc.count_bytes(file_string) == 22

def test_count_chars(file_string):
    assert pywc.count_chars(file_string) == 10

def test_add_none():
    assert pywc.add_none(None, None) == 0
    assert pywc.add_none(1, None) == 1
    assert pywc.add_none(None, -1) == -1
    assert pywc.add_none(1, -1) == 0

def test_to_string():
    assert pywc.to_string(
        1,
        6,
        26,
        None,
        'fake.txt'
    ) == '       1       6      26 fake.txt'

def test_disambiguate_will_only_return_chars_if_both_chars_and_bytes():
    lines = True
    words = True
    bytes_ = True
    chars = True
    filename = 'fake.txt'

    assert pywc.disambiguate(
        lines,
        words,
        bytes_,
        chars,
        filename=filename
        ) == (
            True,
            True,
            False,
            True,
            filename
        )

def test_disambiguate_will_return_bytes_if_bytes_but_not_chars():
    lines = True
    words = True
    bytes_ = True
    chars = False
    filename = 'fake.txt'

    assert pywc.disambiguate(
        lines,
        words,
        bytes_,
        chars,
        filename=filename
        ) == (
            True,
            True,
            True,
            False,
            'fake.txt'
        )

def test_perform_counts_throws_exception_if_passed_no_file_object():
    (
        lines,
        words,
        bytes_,
        chars,
        filename,
        fin
    ) = (
        True,
        True,
        False,
        True,
        'fake.txt',
        None
    )
    with pytest.raises(ValueError):
        pywc.perform_counts(lines, words, bytes_, chars, filename, fp=fin)

def test_perform_counts_standard_options():
    filename = 'tests/ch.txt'
    with open(filename, 'rb') as fin:
        lines, words, bytes_, chars = True, True, False, True
        (
            line_count,
            word_count,
            byte_count,
            char_count,
            filename
        ) = pywc.perform_counts(
            lines,
            words,
            bytes_,
            chars,
            filename=filename,
            fp=fin
        )
        assert line_count == 3
        assert word_count == 4
        assert byte_count is None
        assert char_count == 10
