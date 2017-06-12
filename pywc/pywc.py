# -*- coding: utf-8 -*-


def count_lines(file_string):
    "Return number of lines in file"
    f = file_string.strip('\n')
    f = f.split('\n')
    size = len(f)

    return size

def count_words(file_string):
    "Return number of words in file"
    f = file_string.split()
    size = len(f)

    return size

def count_bytes(file_string):
    "Return number of bytes in file"
    f = file_string.decode('utf-8').encode('utf-8')
    size = len(f)

    return size

def count_chars(file_string):
    "Return number of characters in file"
    f = file_string.decode('utf-8')
    size = len(f)

    return size

def add_none(one, two):
    "Add two to one or 0 if None"
    if not one:
        one = 0
    if not two:
        two = 0
    return one + two



def to_string(line_count, word_count, byte_count, char_count, filename):
    "Return string formatted output"
    c, l, m, w = '', '', '', ''

    if line_count:
        l = '{:>8}'.format(line_count)
    if word_count:
        w = '{:>8}'.format(word_count)
    if byte_count:
        c = '{:>8}'.format(byte_count)
    if char_count:
        m = '{:>8}'.format(char_count)

    return "{}{}{}{} {}".format(
        l, w, c, m,
        filename
    )

def perform_counts(lines, words, bytes_, chars, filename=None, fp=None):
    """
    Return a tuple of counts of lines, words, bytes and chars as well as
    filename for each if passed arguments are True
    """
    if not fp:
        raise ValueError('fp not provided to perform_counts')

    read_file_object = fp.read()

    line_count, byte_count, word_count, char_count = None, None, None, None

    if lines:
        line_count = count_lines(read_file_object)

    if words:
        word_count = count_words(read_file_object)

    if bytes_:
        byte_count = count_bytes(read_file_object)

    if chars:
        char_count = count_chars(read_file_object)


    return line_count, word_count, byte_count, char_count, filename

def disambiguate(lines, words, bytes_, chars, filename=None):
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

    if (not bytes_) and (not chars) and (not lines) and (not words):
        lines, words, bytes_ = True, True, True

    if chars:
        bytes_ = False

    return lines, words, bytes_, chars, filename
