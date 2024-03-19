# 🐘 text map reduce

map reduce scripts for unigrams and bigrams count with optional text cleaning

## usage
```
cat [text file name] | python3 mapper.py [count type] | sort -k1,1 | python3 reducer.py
```
- replace \[text file name\] with path to your text file
- replace \[count type\] with either unigram or bigram
- add `--clean` after \[count type\] if text cleaning is required
