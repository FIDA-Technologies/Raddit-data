import pandas as pd
import numpy as np
import requests
import praw
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

client_ID = 'jRRw9hMnJBVXfQ'
secret_key = 'nkFXjrzRGLMf54iwJOjsdvnWQDbyMQ'

# User　Name: hg558636565
# Pass Word: hg55863656365

reddit = praw.Reddit(client_id = client_ID,
                     client_secret = secret_key,
                     password='hg55863656365',
                     user_agent="RyanAPI/hg558636565",
                     username='hg558636565')

# Get post title and other informations.
posts = []
ml_subreddit = reddit.subreddit('wallstreetbets')

# limit could change to 'all'. means get all the post.
for post in ml_subreddit.hot(limit=10):
    # Sentiment Score
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(title)
    for k in ss:
        print('{0}:{1},'.format(k,ss[k]), end='')
        if k == 'compound':
            posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created, ss[k]])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'sentiment'])

# Get Comments
# id value is each post id. you could write a loop to download it.
submission = reddit.submission(id="likmpp")
submission.comments.replace_more(limit=0)
comm = []
for top_level_comment in submission.comments:
    comm.append(top_level_comment.body)
    
    
