import json
import sys


def main():

    # Read tweets in a list
    list_tweet = []
    dict_hashtags = {}

    # Read tweets in a list
    with open(sys.argv[1], encoding='utf-8') as tweet_file:
        for line in tweet_file:
            dict_tweet = json.loads(line)
            list_tweet.append(dict_tweet)

    # find count of hashtags
    for tweet in list_tweet:
        if "entities" in tweet and "hashtags" in tweet["entities"] and tweet["entities"]["hashtags"]:
            hashtags = tweet["entities"]["hashtags"]
            for ht in hashtags:
                text = ht["text"]
                if text in dict_hashtags:
                    dict_hashtags[text] = dict_hashtags[text] + 1
                else:
                    dict_hashtags[text] = 1

    # sort dictionary in reverse order
    sorted_list = sorted(dict_hashtags.items(),
                         key=lambda t: t[1], reverse=True)

    # display only top 10 hashtags and counts
    for i in range(10):
        hashtag, count = sorted_list[i]
        print(hashtag, count)


if __name__ == "__main__":
    main()
