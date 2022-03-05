#!/usr/bin/env python

# import sys because we need to read and write data to STDIN and STDOUT
import sys

# import re to help remove special characters from text
import re

# import argparse to help parse commandline arguments
import argparse


def clean_text(text, clean=False):
    if not clean:  # don't want to clean
        return text
    # make string lower case
    text_lower = text.lower()
    # remove special characters from string
    return re.sub(r"[^A-Za-z0-9]", " ", text_lower)


def process_line(line, clean=False):
    # to remove leading and trailing whitespace
    line = line.strip()
    line = clean_text(line, clean)
    # split the line into words
    return line.split()


def map_unigram(clean=False):
    # reading entire line from STDIN (standard input)
    for line in sys.stdin:
        words = process_line(line, clean)
        # we are looping over the words array and printing the word
        # with the count of 1 to the STDOUT
        for word in words:
            # write the results to STDOUT (standard output);
            # what we output here will be the input for the
            # reduce step, i.e. the input for reducer.py
            print(f"{word}\t1")


def map_bigram(clean=False):
    # reading entire line from STDIN (standard input)
    for line in sys.stdin:
        words = process_line(line, clean)
        # we are looping over bigram array and printing the bigram
        # with the count of 1 to the STDOUT
        for word, next_word in zip(words, words[1:]):
            # write the results to STDOUT (standard output);
            # what we output here will be the input for the
            # reduce step, i.e. the input for reducer.py
            print(f"{word}-{next_word}\t1")


parser = argparse.ArgumentParser(
    description="hadoop map-reduce mapper which count word occurrence"
)
parser.add_argument(
    "count_type", metavar="count_type", type=str, help="unigram or bigram"
)
parser.add_argument(
    "--clean", action="store_true", help="whether to clean texts before counting"
)

args = parser.parse_args()

count_type = args.count_type
clean = args.clean


if count_type == "unigram":
    map_unigram(clean)
elif count_type == "bigram":
    map_bigram(clean)
