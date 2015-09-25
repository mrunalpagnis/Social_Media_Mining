#!/usr/bin/env python
# -*- coding: utf-8 -*-
#######################
__version__ = "0.1"
__date__ = "Sept. 10, 2015"
__author__ = "Muhammad Abdul-Mageed"
####################################
import argparse
import codecs
import time
import sys
import os, re
import nltk
from collections import defaultdict
from random import shuffle

def getListOfLines():
    """
    Just takes a file and returns a list of its line
    """
    #hard-coding path to inputfile for now
    infileObject=codecs.open("path to file", "r", "utf-8") # you can also have the script receive the input file on the command line via using "sys.argv[1]" more on this next time...
    listOfLines= infileObject.readlines()
    return listOfLines


lines=getListOfLines()
#print "Raw lines:               ", len(lines)
emotionLines= [line.lower() for line in lines if len(line.split("\t"))==4]
#print "Lines of len=4 fields:   ", len(emotionLines)
#print emotionLines[:3]
firstThreeLines=emotionLines[:3]
# TEST:
print"*"*100
# for i in firstThreeLines:
#     tweetId, screenName, userName, tweet = i.split("\t")
#     print tweetId, screenName, userName, tweet

#####################################
tags= ["#happy", "#sad", "#disgusted", "#fearful" , "#surprised", "#angry"] #"#scared"

def tagInSecondHalf(tag, tweet):
    """
    Conditioning position of tag in tweet.
    P.S. Won't consider a tag like #happyday.
    """
    tweet=tweet.split()
    if tag not in tweet:
        return False
    midPoint=(len(tweet)/2)
    tagIndex=tweet.index(tag)
    if tagIndex > midPoint:
        return True
    return False
     
def pure(tag, tweet):
    tagList= ["#sensual", "#sexy", "#nervous","#frustrated", "#stressed", "#horny", "#irritated", "#depressed", "#annoyed"]# "#excited", "#happy", "#sad", "#disgusted", "#fearful" , "#surprised", "#angry", "#scared"]
    tagList.remove(tag)
    for t in tagList:
        if t in tweet: 
            return False
    return True

def removeSeed(seed, tweet):
    """
    """
    if type(seed)==str:
        tweet= re.sub(seed, " ", tweet)
    elif type(seed)==list:
        for t in seed:
            tweet= re.sub(t, " ", tweet)
    else:
        print "arg1/Tag must be a string or list, you provided ", type(tag), "."
        exit()
    #clean
    tweet=re.sub("\s+", " ", tweet)
    tweet=tweet.rstrip()
    tweet=tweet.lstrip()
    return tweet
        

#----------------------------------------------
shuffle(emotionLines)
emotionLines=emotionLines#[:200000]

tagLexicon= ["happy", "sad", "disgusted", "fearful" , "surprised", "angry", "scared"] #"#scared"
myData={}
for cat in tagLexicon:
    tag="#"+cat
    myData[cat]=[tweet for tweet in emotionLines if tag in tweet.split() and pure(tag, tweet)
                 and tagInSecondHalf(tag, tweet) and len(tweet.split()) > 4
                 and removeSeed(tag, tweet)]
#----------------------------------------------
#----------------------------------------------
# lump "fearful" with "scared"
for k in myData:
    if k=="fearful":
        myData["scared"].append(myData[k])

myData.pop("fearful", None)
# Print some stats:
##########################
print "*"*50, "\n"


for k in myData:
    print k, len(myData[k])

##########################################