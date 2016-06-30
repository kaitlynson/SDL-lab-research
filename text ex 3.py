
# coding: utf-8

# In[ ]:

import json
import io # use io.open for outfile or use bz file 
import bz2
import collections as coll
import nltk
from nltk.corpus import cmudict
import string
import math
import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as py_go
import itertools as itr
import glob 


# In[ ]:

SYLLABLE_DICT = cmudict.dict()  


# In[ ]:

def is_three_plus_syllables(word):
    x = SYLLABLE_DICT.get(word.lower())
    if x is None:
        return False
    return len([y for y in x[0] if y[-1].isdigit()]) >= 3

    if len([y for y in x[0] if y[-1].isdigit()]) <= 3:
        return False
    else:
        return True

def count_poly_syllables(sentence):
    words = sentence.split()
    return sum(is_three_plus_syllables(word) for word in words)

def count_sents(sentence):
    return len([''.join(y) for v,y in itr.groupby(sentence, lambda x: x not in '.!?') if v])
        
def compute_smog_score(list_tweets):
    grade = 0
    tot_num_pollys = 0
    total_num_sentences = 0

    for tweet in list_tweets:
        total_num_sentences += count_sents(tweet)
        tot_num_pollys += count_poly_syllables(tweet)

    if total_num_sentences <30: 
        print "too few tweets"
        return None

    else:
        grade = 1.0430*(math.sqrt(tot_num_pollys*(30.0/total_num_sentences))) + 3.1291
        return grade


# In[ ]:

in_file_name = "/Users/sports195admin/Downloads/success_timelines_00002.json.bz2"
out_file_name = "/Users/sports195admin/Downloads/tweets_00001.json.bz2"

with bz2.BZ2File(in_file_name) as infile, bz2.BZ2File(out_file_name, 'w') as outfile:

    for line in infile: 

        first_tab = line.index("\t") # location of first tab char
        id = line[:first_tab]

        tweets = json.loads(line[first_tab:]) # creates a dict

        user_id = tweets[u'user'][0]["id_str"] # gets user id as string

        list_propics = [x['profile_image_url'] for x in tweets[u'user']]

        list_desc = [x['description'] for x in tweets[u'user']]

        list_tweets = [x['text'] for x in tweets[u'tweets']] # makes all the user's tweets into a list

        tdict = coll.OrderedDict() 
        tdict["uid"] = user_id
        tdict["descriptions"] = list_desc
        tdict["texts"] = list_tweets
        tdict["pics"] = list_propics

        # use json lib to turn dict into json dict/list/string

        outfile.write(json.dumps(tdict)+'\n')
        
  


# In[ ]:

#total_num_words = 0
list_smogs = []
list_file_name = glob.glob("/Users/sports195admin/Downloads/tweets_*.bz2")
for document in list_file_name:
    new_in_file_name = document
with bz2.BZ2File(new_in_file_name) as infile:
    for i, line in enumerate(infile):
        user_dict = json.loads(line)
        list_tweets = user_dict["texts"]
        list_smogs.append(compute_smog_score(list_tweets)) # this line wont work..
print np.mean(list_smogs)
print np.std(list_smogs)

list_smogs_s = pd.Series(list_smogs)
print list_smogs_s.max()
print list_smogs_s.min()
print list_smogs_s.mean()
print list_smogs_s.std()


# In[ ]:

data = [
    py_go.Histogram(
        x= list_smogs
    )
]
py.iplot(data)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



