import tweepy
import time

FILE_NAME = 'last_seen.txt'
FILE_TWO_NAME = 'last_seen_date.txt'

CONSUMER_KEY = 'YT3z9njUyWUL71HopPcRyk4sy'
CONSUMER_SECRET = 'K1GYzJFH3TxOgGIhmPPs7YdcVm6lFQP4jyk6xufwY5BllRiFlC'
ACCESS_KEY = '1357094272621756418-QAMdWUBxpTrJKh3Due4eypTz1xPrUS'
ACCESS_SECRET = 'fqy164SSC7hlccbn4QnFwIVIMuCE5bcKqhBePYrJBFWvK'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)




# print(tweets[0].text)

def get_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id= int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return



def get_last_seen_date(file_two):
    f_read = open(file_two, 'r')
    last_seen_date_id= str(f_read.read().strip())
    f_read.close()
    return last_seen_date_id

def store_last_seen_date(last_seen_date_id, file_two):
    f_write = open(file_two, 'w')
    date = ''
    for ch in str(last_seen_date_id):
        if(ch == ' '):
            break
        date += ch
    f_write.write(str(date))
    f_write.close()


def reply_to_tweets():
    last_seen_id = get_last_seen_id(FILE_NAME)
    last_seen_date_id = get_last_seen_date(FILE_TWO_NAME)

    tweets = api.user_timeline(screen_name = 'ConanOBrien', since_id = last_seen_id, exclude_replies = True, include_rts = False)


    for tweet in reversed(tweets):
        print(str(tweet.id) + ' - ' + tweet.text + ' - ' + str(tweet.created_at))
        last_seen_id = tweet.id
        last_seen_date_id = tweet.created_at
        store_last_seen_id(last_seen_id, FILE_NAME)
        store_last_seen_date(last_seen_date_id, FILE_TWO_NAME)


