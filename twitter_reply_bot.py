import tweepy
import time

FILE_NAME = 'last_seen.txt'

CONSUMER_KEY = 'YT3z9njUyWUL71HopPcRyk4sy'
CONSUMER_SECRET = 'K1GYzJFH3TxOgGIhmPPs7YdcVm6lFQP4jyk6xufwY5BllRiFlC'
ACCESS_KEY = '1357094272621756418-QAMdWUBxpTrJKh3Due4eypTz1xPrUS'
ACCESS_SECRET = 'fqy164SSC7hlccbn4QnFwIVIMuCE5bcKqhBePYrJBFWvK'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



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




def reply_to_tweets():
    last_seen_id = get_last_seen_id(FILE_NAME)

    tweets = api.search(q = "\"under there\"", since_id = last_seen_id)


    for tweet in reversed(tweets):
        print(str(tweet.id) + ' - ' + tweet.text + ' - ' + str(tweet.created_at))
        last_seen_id = tweet.id
        store_last_seen_id(last_seen_id, FILE_NAME)


reply_to_tweets()