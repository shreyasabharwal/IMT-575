import sys
import json
import re
import tweet_sentiment as ts


def hw():
    print('Hello, world!')


def lines(fp):
    print(str(len(fp.readlines())))


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

    list_tweet = []
    dict_sent = {}
    # Read sentiments in a dictionary
    with open(sys.argv[1]) as sent_file:
        for line in sent_file:
            dict_sent.update(
                {line.split("\t")[0]: line.split("\t")[1].strip()})
    # print(dict_sent)

    # Read tweets in a list
    with open(sys.argv[2]) as tweet_file:
        for line in tweet_file:
            dict_tweet = json.loads(line)
            list_tweet.append(dict_tweet)

    # Calculate Score of each tweet - calculated already in tweet_Sentiment.py
    scores = ts.calculateScore(list_tweet, dict_sent)

    # Calculate score of individual word not present in sentiment file
    new_terms_scores = calculate_score_new_terms(list_tweet, dict_sent, scores)

    # Print to Stdout
    for term, score in new_terms_scores.items():
        print(term, score)


def calculate_score_new_terms(list_tweet, dict_sent, scores):

    word_list = []
    new_word_dict = {}
    count = {}

    for i in range(len(list_tweet)):
        score = scores[i]
        if 'text' in list_tweet[i].keys():
            # create a list of words of tweet
            words = re.split(r'\W+', list_tweet[i]['text'])
            words = [word.lower() for word in words if len(word) > 0]
            word_list.extend(words)
            for word in word_list:
                # If word is not present in the sentiment file and new dictionary created, assign score of tweet
                if dict_sent.get(word, 0) == 0 and new_word_dict.get(word, 0) == 0:
                    new_word_dict[word] = score
                    count[word] = 1
                # If word is not present in the sentiment file but already added in new dictionary created, add score of the tweet
                elif dict_sent.get(word, 0) == 0 and new_word_dict.get(word, 0):
                    new_word_dict[word] = new_word_dict[word] + score
                    count[word] = count[word] + 1

    # Taking average of all scores for the term
    for k, v in new_word_dict.items():
        if count[k] != 0:
            new_word_dict[k] = float(v)/float(count[k])

    return new_word_dict


if __name__ == '__main__':
    main()
