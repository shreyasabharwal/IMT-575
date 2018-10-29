import json
import re
import sys


def main():
    file_name = sys.argv[1]

    # Read tweets in a list
    list_tweet = []
    with open(sys.argv[1], encoding='utf-8') as tweet_file:
        for line in tweet_file:
            dict_tweet = json.loads(line)
            list_tweet.append(dict_tweet)

    word_list = create_word_list(list_tweet)

    frequency_dict = calculate_frequency(word_list)

    for word, freq in frequency_dict.items():
        print(word, freq)

# create list of words


def create_word_list(list_tweet):
    word_list = []
    for tweet in list_tweet:
        if 'text' in tweet.keys():
            words = re.split(r'\W+', tweet['text'])
            words = [word.lower() for word in words if len(word) > 0]
            word_list.extend(words)
    return word_list


# calculate frequency of each word


def calculate_frequency(word_list):
    word_frequency = {}
    for word in word_list:
        if word_frequency.get(word, 0):
            word_frequency[word] = word_frequency[word] + 1
        else:
            word_frequency[word] = 1

    total_freq = sum(word_frequency.values())

    for freq in word_frequency:
        word_frequency[freq] = word_frequency[freq]/total_freq
    return word_frequency


if __name__ == '__main__':
    main()
