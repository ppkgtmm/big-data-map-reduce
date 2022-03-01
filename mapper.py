#!/usr/bin/env python
  
# import sys because we need to read and write data to STDIN and STDOUT
import sys
# import re to help remove special characters from text
import re

def clean_word(word, clean=False):
    if not clean: # don't want to clean
        return word
    # make word lower case
    word_lower = word.lower()
    # remove special characters from word
    return re.sub(r'[^A-Za-z0-9]', '', word_lower)

def process_line(line, clean=False):
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words, clean words and remove empty words from cleaning
    return [clean_word(w, clean) for w in line.split() if clean_word(w, clean)]

def map_unigram(clean=False):
    # reading entire line from STDIN (standard input)
    for line in sys.stdin:
        words = process_line(line, clean)
        # we are looping over the words array and printing the word
        # with the count of 1 to the STDOUT
        for word in words:
            # write the results to STDOUT (standard output);
            # what we output here will be the input for the
            # Reduce step, i.e. the input for reducer.py
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
            # Reduce step, i.e. the input for reducer.py
            print(f"{word}-{next_word}\t1")

if len(sys.argv) < 2:
    print(
        '\nUsage: python3 file_name.py count_type [clean]\n\n\
        count_type\tunigram or bigram\n\
        clean\t\tspecify t if you want to clean words\n'
    )
    sys.exit(1)

clean = False
if len(sys.argv) > 2 and sys.argv[2] == 't':
    clean = True

if sys.argv[1] == 'unigram':
    map_unigram(clean)
elif sys.argv[1] == 'bigram':
    map_bigram(clean)
