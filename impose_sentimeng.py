import pandas as pd
import numpy as np
import seaborn as se
import datetime
import math
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# import data.
data = pd.read_csv("C:\\Users\\qxu5\\Desktop\\reddit\\GME_Post.csv")
del data['Unnamed: 0']
data = data.sort_values(by = ['year', 'month', 'day', 'hour'])
data.index = range(len(data))
data = data.iloc[0:11183,:]


# Add Title sentiment.
sid = SentimentIntensityAnalyzer()
title = []
for each in range(len(data)):
    if type(data.loc[each, 'title']) == str:
        title.append(sid.polarity_scores(data.loc[each, 'title'])['compound'])
    else:
        title.append(data.loc[6, 'title'])
data['Title_sentiment'] = title

# Get comments sentiment.
com_score = []
com = []
posttime = []
ID = []
data['Top_comments'] = data['Top_comments'].fillna('0')
for post1 in range(len(data)):
    if data['Top_comments'][post1] != '0':
        catch = data['Top_comments'][post1].split('], [')
        for each in catch:
            if each != '[]':
                crop = each.split('datetime.datetime')
                com_score.append(sid.polarity_scores(crop[0])['compound'])
                com.append(crop[0])
                d = each.split('datetime.datetime')[1]
                d = d.replace(']','')
                d = d.replace('(','')
                d = d.replace(')','')
                d = d.split(', ')
                time = d[1]+'/'+d[2]+'/'+d[0]+' '+d[3]+':'+d[4]
                posttime.append(datetime.datetime.strptime(time, '%m/%d/%Y %H:%M'))
                ID.append(data['ID'][post1])
comm = pd.DataFrame({"comments":com, "Comment_sentiment":com_score, 'ID':ID, 'Post_Time':posttime})
comm['year'] = comm['Post_Time'].dt.year
comm['month'] = comm['Post_Time'].dt.month
comm['day'] = comm['Post_Time'].dt.day
comm['hour'] = comm['Post_Time'].dt.hour

new = pd.merge(data, comm, on = ['year', 'month', 'day', 'hour'], how = 'outer')
ll = new[['year', 'month', 'day', 'hour', 'Title_sentiment', 'Comment_sentiment']].groupby(['year', 'month', 'day', 'hour']).mean()
kk = ll.index.to_frame()
kk['Title_sentiment'] = ll['Title_sentiment']
kk['Comment_sentiment'] = ll['Comment_sentiment']
kk.index = range(len(kk))

final = pd.merge(kk,new[['year', 'month', 'day', 'hour', 'return']], on = ['year', 'month', 'day', 'hour'], how = 'outer')
final = final.drop_duplicates()
final['Title_sentiment'] = final['Title_sentiment'].fillna(0)
final['Comment_sentiment'] = final['Comment_sentiment'].fillna(0)
final['senti'] = final['Title_sentiment'] + final['Comment_sentiment']

















