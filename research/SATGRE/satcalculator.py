# coding: utf-8
# Kaitlyn Son


## last updated sept 27 


import json
import io
import bz2
import collections as coll
import nltk
from nltk.corpus import cmudict
import string
import math
import numpy as np
import pandas as pd
from string import maketrans
import regex as re
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('ks772', 'x27zf4qmhv') ## what is my u and key..



## creating a SAT word list from a text file
sat_word_list = []
with open('/Users/sports195admin/Desktop/rxch/github/research/SATGRE/SATWords.txt', 'r') as infile:
    for line in infile:
        sat_word_list.append(line.strip("\n").split()[0]) # add first word of every line to list


## creating a GRE word list from a text file
# gre_word_list = []
# with open('/Users/sports195admin/Desktop/rxch/SATGRE/GREwordlist.txt', 'r') as infile:
#     for line in infile:
#         gre_word_list.append(line.strip("\n").split()[0]) # add first word of every line to list


# removes punctuation
# takes a string only tho 
def remove_punctuation(text):
    #pat = re.compile(ur"[\p{P}\p{S}]+")
    pat = re.compile(ur"[\p{P}\p{S}](?<!-)+")
    return pat.sub("", text)


in_file_name = "/Users/sports195admin/Downloads/success_timelines_00000.json.bz2"
out_file_name = "/Users/sports195admin/Downloads/tweets_00000.json.bz2"

with bz2.BZ2File(in_file_name) as infile, bz2.BZ2File(out_file_name, 'w') as outfile:
    list_of_sat_nums = []   
    for line in infile: 

        first_tab = line.index("\t") # location of first tab char
        first_tab
        id = line[:first_tab]
        id #users id

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

        outfile.write(json.dumps(tdict)+'\n')
        
        # goes thru every user and finds sat words
        
        sample = list_tweets

        usable_sample = ""

        ## strips all punctuation and makes everything lowercase 
        for line in sample:
            usable_sample += remove_punctuation(line.lower())

        sat_word_set = set(sat_word_list)

        words = usable_sample.split() 
        print words 

        sat_word_count = sum(word in sat_word_set for word in words)

        ####print sat_word_count
        #%time
        list_of_sat_nums.append(sat_word_count)

#print list_of_sat_nums # this prints the list of all the "Sat scores" 



x = list_of_sat_nums

data = [
    go.Histogram(
        x=list_of_sat_nums
    )
]
py.iplot(data)

# look slike 120-170 is the most popular score

## need percentage of sat words then plot it 
# find num of words in total
# divide that by num sat words

# use glob.glob to pull info from all files not just one 


# make a scatterplot of smog scores vs sat scores for users and compute the correlation.
# gre version

