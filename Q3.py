def findWordsWithFrequency(n, wordList):
    if (n == 0):
        return []

    word_frequencies = []
    ret_list = []

    # creating a list to store the count of each word in the list
    for i in wordList:
        word_frequencies.append(wordList.count(i))

    for i in range(len(word_frequencies)):
        # compare the count of the word in the specific index to the given n and append it to the list if it matches
        if word_frequencies[i] >= n and wordList[i] not in ret_list:
            ret_list.append(wordList[i])

    return ret_list

