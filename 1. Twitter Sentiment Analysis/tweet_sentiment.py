import sys
import json
import re


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

    # Read tweets in a list
    with open(sys.argv[2], encoding='utf-8') as tweet_file:
        for line in tweet_file:
            dict_tweet = json.loads(line)
            list_tweet.append(dict_tweet)

    # Calculate Score of each tweet
    scores = calculateScore(list_tweet, dict_sent)

    # stdout
    for score in scores:
        sys.stdout.write(str(score)+'\n')


def calculateScore(list_tweet, dict_sent):

    list_score = []
    for tweet in list_tweet:
        tweet_score = 0
        if 'text' in tweet.keys():
            # create a list of words
            word_list = re.split(r'\W+', tweet['text'])
            for word in word_list:
                if dict_sent.get(word, 0):
                    # if word is already present in the sentiment file, add the score to the tweet score
                    tweet_score = tweet_score + int(dict_sent[word])
        else:
            tweet_score = 0

        list_score.append(tweet_score)
    return list_score


if __name__ == '__main__':
    main()
