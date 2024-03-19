# word count map reduce

Repo created to store code for word count MapReduce task assigned in lab of course CPE 325 Big Data, King Mongkut's University of Technology Thonburi. Supported MapReduce tasks are namely counting unigrams and bigrams. Texts can be optionally cleaned prior to MapReduce

## Walk through
- [mapper](https://github.com/ppkgtmm/big-data-map-reduce/blob/main/mapper.py) counts words inside input text which is supplied line by line
- [reducer](https://github.com/ppkgtmm/big-data-map-reduce/blob/main/reducer.py) combines counts for each distinct word inside text

## Usage
- Count unigrams without text cleaning
```sh
cat [text file name] | python3 mapper.py unigram | sort -k1,1 | python3 reducer.py
```
- Count bigrams with text cleaning
```sh
cat [text file name] | python3 mapper.py bigram --clean | sort -k1,1 | python3 reducer.py
```

see this [notebook](https://github.com/ppkgtmm/big-data/blob/main/Lecture%206%20-%20Hadoop%20MapReduce/Exercise.ipynb) if you want to know more about how the code here is used with hadoop

## References
- [Hadoop streaming using python word count problem](https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/)
- [Command line interfaces python argparse](https://realpython.com/command-line-interfaces-python-argparse/)
