import tweepy

consumer_key = 'iYuXDDCGpHK21IKsdPHp2SGyC'
consumer_secret = 'WS0VRAEgucLPMUC4sPHkR6paNWUWjnQMD9Sa69dLMsbYnSoGSl'
access_token = '1059635773832654849-dXbjvut3bhqxSiz3ELj1mVW3PN6qXR'
access_token_secret = 'xDOSZMwZkBZrlDMjrVA7liAcnS0zCxu6qchzqdOOJr6AL'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('@realDonalTrump')
print(user,'\n')
print(user.screen_name)
print(user.followers_count)