#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_cli
----------------------------------

CLI Tests for `pywc` module.
"""

from click.testing import CliRunner
from pywc import cli

def test_cli_help():
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message and exit.' in help_result.output

def test_cli_zero_files_fails():
    "This should fall back to stdin, but for now it should though an exception"
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert 'Error: Missing argument "files"' in result.output
    assert result.exit_code != 0

def test_cli_one_file_zero_options():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['tests/test.txt'])
    assert '      3      12      96 tests/test.txt' in result.output
    assert result.exit_code == 0

def test_cli_two_files_zero_options():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['tests/test.txt', 'tests/ch.txt'])
    assert '      3      12      96 tests/test.txt' in result.output
    assert '      3       4      22 tests/ch.txt' in result.output
    assert '      6      16     118 total' in result.output
    assert result.exit_code == 0

def test_cli_one_file_lines():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--lines', 'tests/ch.txt'])
    assert result.output == '       3 tests/ch.txt\n'
    assert result.exit_code == 0

def test_cli_one_file_words():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--words', 'tests/test.txt'])
    assert result.output == '      12 tests/test.txt\n'
    assert result.exit_code == 0

def test_cli_one_file_bytes():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--bytes', 'tests/test.txt'])
    assert result.output == '      96 tests/test.txt\n'
    assert result.exit_code == 0

def test_cli_one_file_chars():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--bytes', 'tests/test.txt'])
    assert result.output == '      96 tests/test.txt\n'
    assert result.exit_code == 0
