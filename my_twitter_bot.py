import tweepy
import time


print ("This is my twitter bot")

# these are list of keys provided from twitter using Keys and Tokens tab on Application
# this is set of Consumer API Keys
CONSUMER_KEY = 'ZKD9lwfLYRY2eRxySFrWGuO54'
CONSUMER_SECRET = 'baOGOSUzgoivIn4uptBdMKfGLOKBa0Iqr2KbjVtka9A5imvSE1'

# this is a set of Access Tokens 
ACCESS_KEY = '584563130-8ILa1VdCeSsiXmprTFpEGFMW2qpcgxpO8VUyZxB5'
ACCESS_SECRET = 'fyxlaxtrSyNEm8DIB19nXiqGCxOaiAFRyTpkxst5x9grr'

# authenticate these keys and tokens to the app
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name): # function used to read a text file using readfiles()
	f_read = open(file_name, 'r')
	last_seen_id = int(f_read.read().strip())
	f_read.close()
	return last_seen_id

def store_last_seen_id(last_seen_id, file_name): # function used to store/write value to a textfile
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return

def reply_to_tweets():
	print('retrieving and replying to tweets')
	last_seen_id = retrieve_last_seen_id(FILE_NAME)
	mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')

	for mention in reversed(mentions):
		print(str(mention.id) + ' - ' + mention.full_text)
		last_seen_id = mention.id
		store_last_seen_id(last_seen_id, FILE_NAME)
		if '#helloworld' in mention.full_text.lower():
			print("found #helloworld")
			print("responding back ! ")
			api.update_status('@' + mention.user.screen_name + ' Test Message', mention.id)


while True:
	reply_to_tweets()
	time.sleep(5)