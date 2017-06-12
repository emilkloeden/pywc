# -*- coding: utf-8 -*-

import click
import pywc
import sys
import os


@click.command()
@click.option('--bytes', '-c', is_flag=True, help="""
The number of bytes in each input file is written to the standard
output.  This will cancel out any prior usage of the -m option.""")
@click.option('--lines', '-l', is_flag=True, help="""
The number of lines in each input file is written to the standard
output.""")
@click.option('--chars', '-m', is_flag=True, help="""
The number of characters in each input file is written to the
standard output.  If the current locale does not support multi-
byte characters, this is equivalent to the -c option.  This will
cancel out any prior usage of the -c option.""")
@click.option('--words', '-w', is_flag=True, help="""
The number of words in each input file is written to the standard
output.""")

@click.argument('files', type=click.Path(exists=True), nargs=-1, required=True)
def main(bytes, chars, lines, words, files):
    """
    When an option is specified, wc only reports the information requested by
    that option.  The order of output always takes the form of line, word,
    byte, and file name.  The default action is equivalent to specifying the
    -c, -l and -w options.

    If no files are specified, the standard input is used and no file name is
    displayed.  The prompt will accept input until receiving EOF, or [^D] in
    most environments.
    """

    total_lines = total_words = total_bytes = total_chars = 0


    for filename in files:
        with open(filename, 'rb') as fp:
            tuple_ = pywc.disambiguate(
                lines,
                words,
                bytes,
                chars,
                filename
                )
            tuple_ = pywc.perform_counts(*tuple_, fp=fp)

            line_count, word_count, byte_count, char_count, filename = tuple_
            total_lines = pywc.add_none(total_lines, line_count)
            total_words = pywc.add_none(total_words, word_count)
            total_bytes = pywc.add_none(total_bytes, byte_count)
            total_chars = pywc.add_none(total_chars, char_count)

            # echo to stdout
            click.echo(pywc.to_string(*tuple_))

    if len(files) > 1:
        # echo total row if more than one file given
        click.echo(pywc.to_string(total_lines, total_words, total_bytes, total_chars, 'total'))
    """
    else:
        tuple_ = pywc.disambiguate(
            bytes_,
            chars,
            lines,
            words,
            files,
            filename=None
        )
        click.echo(pywc.to_string(*tuple_))
    """
    """
    for f in files:
        click.echo(len(f.readlines()))
    """

if __name__ == "__main__":
    main()
