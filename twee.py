#! /usr/bin/python

import tweepy
 

auth = tweepy.OAuthHandler("VnI1GB32dpHJBpmpxFKyopr98", "H9Vki7yX8qBegCzKU9Umg3MUvHAXWKtYgiQj2XDYwrobeaGsvT")
auth.set_access_token("300996006-R9JRp30nO79m974kDtgGDqZxv6d2RLhqi4DifBSD"
 ,"YbgUHnIgHtX1JjcE8f7PpJw5CTMtjb7yhPp3vlyxBP20I")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  cfg = {
    "consumer_key"        :"VnI1GB32dpHJBpmpxFKyopr98",
    "consumer_secret"     :"H9Vki7yX8qBegCzKU9Umg3MUvHAXWKtYgiQj2XDYwrobeaGsvT",
    "access_token"        : "300996006-R9JRp30nO79m974kDtgGDqZxv6d2RLhqi4DifBSD",
    "access_token_secret" : "YbgUHnIgHtX1JjcE8f7PpJw5CTMtjb7yhPp3vlyxBP20I" 
    }

  api = get_api(cfg)
  tweets = api.home_timeline()
  print("@@@")
  print(tweets[0])

  tweet = "hmmm, i need russel westbrook's energy drink"
  status = api.update_status(status=tweet)

if __name__ == "__main__":
  main() 
