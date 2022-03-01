#!/usr/bin/env python
  
# import sys because we need to read and write data to STDIN and STDOUT
import sys
# import re to help remove special characters from text
import re

# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
      
    # we are looping over bigram array and printing the bigram
    # with the count of 1 to the STDOUT
    for word, next_word in zip(words, words[1:]):
        # make words lower case
        word_lower = word.lower()
        next_word_lower = next_word.lower()
        # remove special characters from words
        # after removal if words are empty strings replace them with space
        word_sub = re.sub(r'[^A-Za-z0-9]', '', word_lower) or ' '
        next_word_sub = re.sub(r'[^A-Za-z0-9]', '', next_word_lower) or ' '
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        print(f"{word_sub}-{next_word_sub}\t1")