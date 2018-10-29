import json
import re
import sys
import state_abbreviations as st
import tweet_sentiment as ts


def state_codes(country):
    st_dict = st.states
    for code, ctry in st_dict.items():
        if (ctry == country):
            return code
    return None

# find happiest state


def get_happiest_state(dict_state_scores, dict_state_twtcount):

    for key in dict_state_scores:
        # averaging the scores - score/num of tweets for the state
        dict_state_scores[key] = dict_state_scores[key] / \
            dict_state_twtcount[key]

    state = max(dict_state_scores, key=lambda k: dict_state_scores[k])
    return state


def main():

    # Read tweets in a list
    list_tweet = []
    dict_sent = {}
    dict_state_scores = {}
    dict_state_twtcount = {}

    with open(sys.argv[1]) as sent_file:
        for line in sent_file:
            dict_sent.update(
                {line.split("\t")[0]: line.split("\t")[1].strip()})

    # Read tweets in a list
    with open(sys.argv[2], encoding='utf-8') as tweet_file:
        for line in tweet_file:
            dict_tweet = json.loads(line)
            list_tweet.append(dict_tweet)

    list_scores = ts.calculateScore(list_tweet, dict_sent)

    for i in range(len(list_tweet)):
        tweet = list_tweet[i]
        found_state = False

        # getting country code from place object
        if "place" in tweet and tweet["place"] is not None:
            place = tweet["place"]
            if "country_code" in place and place["country_code"] == "US":
                # Name = 'California'
                if "place_type" in place and place["place_type"] == "admin":
                    code = state_codes(place["name"])
                    # print("name", code)
                    found_state = True

                # Full Name = 'Los Angeles, CA'
                if found_state == False and "place_type" in place and place["place_type"] == "city":
                    full_name = place["full_name"]
                    word_list = full_name.strip().split(" ")
                    code = word_list[-1]
                    # print("full name", code)
                    found_state = True

        # getting location from place object
        if found_state == False and "user" in tweet and tweet["user"] is not None and "location" in tweet["user"]:
            location = tweet["user"]["location"]
            if location is not None:
                word_list = location.strip().split(" ")
                word = word_list[-1]
                if state_codes(word) is not None:
                    code = state_codes(word)
                    # print("loc", code)
                    found_state = True

        if found_state == True:
            if code not in dict_state_scores:
                dict_state_scores[code] = list_scores[i]
                dict_state_twtcount[code] = 1
            else:
                dict_state_scores[code] = dict_state_scores[code] + \
                    list_scores[i]
                dict_state_twtcount[code] = dict_state_twtcount[code] + 1

    happiest_state = get_happiest_state(dict_state_scores, dict_state_twtcount)

    print(happiest_state)


if __name__ == "__main__":
    main()
