"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    def __init__ (ge, path):
        dict_file = open(path)
        ge.words = ge.parse(dict_file)
        print(f"{len(ge.words)} words are read")
    
    def parse(ge, dict_file):
        return [x.strip() for x in dict_file]
    
    def random(ge):
        return random.choice(ge.words)

class Special(WordFinder):
    def parse(ge, dict_file)
        return [x.strip() for x in dict_file if x.strip() and not x.startswith("#")]
