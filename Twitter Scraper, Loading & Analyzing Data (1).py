
# coding: utf-8

# In[33]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import json      # library for working with JSON-formatted text strings
import pprint as pp    # library for cleanly printing Python data structures
import seaborn as sns


# This is a basic test for https://github.com/taspinar/twitterscraper. Using the demo data looking at all tweets re. Trump. 

# twitterscraper "climate change from:metrolosangeles" --lang en -o cc_test.JSON -l 100

# In[3]:


#this loads the data into json in the notebook

with open('cc_test.JSON') as f:
 data1 = json.load(f)

print(type(data1))


# print(data[:500])

# pp.pprint(data)

# 
# 
# 
# #wordcloud
# 
# 
# 
# 

# In[94]:


#for x in data:
  # print(x['text'])


# In[4]:


d = {'username': [x['username'] for x in data1],
    'time': [x['timestamp'] for x in data1],
    'tweet': [x['text'] for x in data1],
    'likes': [x['likes'] for x in data1],
    'replies': [x['replies'] for x in data1]
    }

df = pd.DataFrame.from_dict(d)
df


# In[31]:


#going to try to create a single function to do this 

def json_to_df_tweets (csv_file):
    with open(csv_file) as f:
      data = json.load(f)
    
    d = {'username': [x['username'] for x in data],
        'time': [x['timestamp'] for x in data],
        'tweet': [x['text'] for x in data],
        'likes': [x['likes'] for x in data],
        'replies': [x['replies'] for x in data]
        }
    
    df_Test = pd.DataFrame.from_dict(d)
    
    return df_Test


# In[32]:


# Twitter data that states "climate change"; the scraper loads in requests by user
la_metro_tweets = json_to_df_tweets ('cc_test.JSON')
lacity_tweets = json_to_df_tweets ('lacity_tweets.json')
ladot_tweets = json_to_df_tweets('ladot_tweets.json')
laplanning_tweets = json_to_df_tweets('laplanning_tweets.json')
laport_tweets = json_to_df_tweets('laport_tweets.json')


# Using the function above "json_to_df_tweets" - we'll load all of the LA City tweets with the words "climate change" so that we can merge them together in one large df. 

# lacity_tweets.json /
# lacountyparks_tweets.json /
# ladot_tweets.json /
# laplanning_tweets.json /
# laport_tweets.json

# In[27]:


def combine_dataframe (df1, df2, df3, df4, df5, df6): #this function smooshes all the dataframes into one using .append()
    d1 = df1.append(df2)
    d2 = d1.append(df3)
    d3 = d2.append(df4)
    d4 = d3.append(df5)
    d5 = d4.append(df6)
    return d5.drop_duplicates(subset='tweet', keep="first") #the scraper picked up dups, this rectifies that


# In[28]:


la_tweets = combine_dataframe(ladot_tweets, la_metro_tweets, lacity_tweets, la_parks_tweets, laplanning_tweets, laport_tweets)
la_tweets


# We have all the tweets from LA city agencies that mention climate change. 

# In[43]:


ax = sns.countplot(x='username', data=la_tweets)
ax.set_xticklabels(labels=['LADOT', 'Metro', 'City', 'Parks', 'Planning', 'Port'], rotation=30)
plt.show()


# In[49]:


la_tweets.sort_values(by= 'time', ascending=True)
#test = sns.tsplot(data=la_tweets, time="time", unit="username", value="likes")

