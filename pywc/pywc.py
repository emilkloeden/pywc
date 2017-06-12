# -*- coding: utf-8 -*-
import sys
import os

#sys.stdin

def count_lines(file_object):
    return len(file_object.readlines())

def count_words(file_object):
    return len(file_object.read().split())

def count_bytes(file_object):
    return len(file_object.read().encode('utf-8'))

def count_chars(file_object):
    return len(file_object.read())


def to_string(line_count, byte_count, word_count, char_count, filename):
    c,l,m,w = '','','',''
    if line_count is not None:
        l = str(line_count).rjust(8)
    if byte_count is not None:
        c = str(byte_count).rjust(8)
    if word_count is not None:
        w = str(word_count).rjust(8)
    if char_count is not None:
        m = str(char_count).rjust(8)

    return "{}{}{}{} {}".format(
        c,l,m,w,
        filename
    )

def disambiguate(bytes_, chars, lines, words, fp, filename=None):
    """
    When an option is specified, wc only reports the information requested by
    that option.  The order of output always takes the form of line, word,
    byte, and file name.  The default action is equivalent to specifying the
    -c, -l and -w options.

    If no files are specified, the standard input is used and no file name is
    displayed.  The prompt will accept input until receiving EOF, or [^D] in
    most environments.

    -c bytes
    -l lines
    -m chars
    -w words
    """
    line_count, byte_count, word_count, char_count = None, None, None, None

    if (not bytes_) and (not chars) and (not lines) and (not words):
        lines, words, bytes_ = True, True, True

    if lines:
        line_count = count_lines(fp)

    if bytes_ and (not chars):
        byte_count = count_bytes(fp)

    if words:
        word_count = count_words(fp)

    if chars:
        char_count = count_chars(fp)


    return line_count, byte_count, word_count, char_count, filename
