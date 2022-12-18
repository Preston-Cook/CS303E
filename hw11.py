# File: WordleAssistant.py
# Student: Preston Cook
# UT EID: plc886
# Course Name: CS303E
#
# Date: 12/17/2022
# Description of Program: Helps the user solve Wordle

def main() -> int:
    word_lst, _ = createWordlist('words.txt')

    print(getPossibleWords(word_lst, {'a': 0, 'b': 1}, 'o', 'v'))
    return 0


def createWordlist(filename: str) -> tuple[list, int]:
    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'. Return
    the list of words and the number of words as a pair. """
    with open(filename, 'r') as f:
        words = f.read().splitlines()

    word_lst = list(filter(isValid, words))

    return (word_lst, len(word_lst))


def isValid(word: str) -> bool:
    return len(word) == 5 and not word.endswith('s') and len(set(word)) == 5


def containsAll(wordlist: list, include: str) -> set:
    """ Given your wordlist, return a set of all words from the wordlist
    that contain all of the letters in the string include. 
    """
    word_set = set()
    for word in wordlist:
        if all(char in word for char in include):
            word_set.add(word)

    return word_set


def containsNone(wordlist: list, exclude: str) -> set:
    """ Given your wordlist, return a set of all words from the wordlist
    that do not contain any of the letters in the string exclude. 
    """
    word_set = set()
    for word in wordlist:
        if all(char not in word for char in exclude):
            word_set.add(word)

    return word_set


def containsAtPositions(wordlist: list, posInfo: dict) -> set:
    """ posInfo is a dictionary that maps letters to positions.
    You can assume that the positions are in [0..4]. Return a set of
    all words from the wordlist that contain the letters from the
    dictionary at the indicated positions. For example, given posInfo
    {'a': 0, 'y': 4}.  This function might return the set:
    {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}. """
    word_set = set()

    for word in wordlist:
        for k, v in posInfo.items():
            if word[v] != k:
                break
        else:
            word_set.add(word)

    return word_set


def getPossibleWords(wordlist: list, posInfo: dict, include: str, exclude: str) -> set:
    """ Finally, given a wordlist, dictionary posInfo, and
    strings include and exclude, return the set of all words from 
    the wordlist that contains the words that satisfy all of 
    the following:
    * has letters in positions indicated in posInfo
    * contains all letters from string include
    * contains none of the letters from string exclude.
    """
    return containsAll(wordlist, include) & containsNone(wordlist, exclude) & containsAtPositions(wordlist, posInfo)


if __name__ == '__main__':
    main()