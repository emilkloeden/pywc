# -*- coding: utf-8 -*-

import click
import pywc
import sys
import os


@click.command()
@click.option('--bytes_', '-c', is_flag=True, help="""
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

@click.argument('filenames', nargs=-1)
def main(bytes_, chars, lines, words, filenames):
    """
    When an option is specified, wc only reports the information requested by
    that option.  The order of output always takes the form of line, word,
    byte, and file name.  The default action is equivalent to specifying the
    -c, -l and -w options.

    If no files are specified, the standard input is used and no file name is
    displayed.  The prompt will accept input until receiving EOF, or [^D] in
    most environments.
    """
    first_file = filenames[0]

    if os.path.isfile(first_file):
        for filename in filenames:
            with open(filename, 'r') as fp:
                tuple_ = pywc.disambiguate(
                    bytes_,
                    chars,
                    lines,
                    words,
                    fp,
                    filename=os.path.basename(filename)
                    )
                click.echo(pywc.to_string(*tuple_))

    else:
        tuple_ = pywc.disambiguate(
            bytes_,
            chars,
            lines,
            words,
            filenames,
            filename=None
        )
        click.echo(pywc.to_string(*tuple_))



if __name__ == "__main__":
    main()
