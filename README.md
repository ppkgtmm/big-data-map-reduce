# 🐘 text map reduce

map reduce scripts for unigrams and bigrams count with optional text cleaning

## usage
```
cat [text file name] | python3 mapper.py [count type] --clean | sort -k1,1 | python3 reducer.py
```
- replace \[text file name\] with path to your text file
- replace \[count type\] with either unigram or bigram
- omit `--clean` if text cleaning is not required

## references
- [hadoop streaming using python word count problem](https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/)
- [command line interfaces python argparse](https://realpython.com/command-line-interfaces-python-argparse/)
