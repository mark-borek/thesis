# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 09:24:31 2020

@author: Mark Borek 
"""

from twitterscraper import query_tweets
import datetime as dt
import csv

#array that will be used for the tweet data objects   
array = []
#array that will be used for the trends objects
trendArray = []
 

#Because of the scope of this project, I manually defined the strings that will define the queries
#All of the topics are related to the topic: Coronavirus  
#The twitterscraper will query for tweets on each of these topics


trends = ['Pandemic','corona','#coronavirus','Coronavirus','quarantine','COVID-19','COVID','#CoronaOutbreak','#Covid_19'
'Wuhan','World health organization','WHO','CDC','testing','flatten the curve','#FlattenTheCurve','#WorkingFromHomeLife',
'Easter','isolation','PPE','social distancing','#WhyIWasQuarantined','6 feet','6ft','respirator','ventilator',
'self-quarantine','Stay-at-home order','stay at home','stay home','stay safe','#StayHomeStaySafe','virus',
'#WhyImStillQuarantined','#PrimaryElection','#remoteworking', '#flatteningthecurve','#CancelEverythingNow',
'#CoronavirusPandemic','#FridayThe13th','#SocialDistance','#coronapocalypse','#NationalEmergency','#TrumpPressConference',
'#QuarantineAndChill','#selfisolationgame','#NetflixAndStayStill','#panicshopping','toilet paper','#StayHome',
'#ThingsYouShouldHoard','shutdown','#StayHomeSaveLives','#LALockdown','#workingfromhome','#homeschooling','#QuarantineLife',
'#NYCLockdown','#TogetherApart','Tom Brady','#StimulusPackage2020','#PPEshortage','#WhenILeaveMyHouseAgain',
'#SocialDistancingPickUpLines','#QuarentineLife','Netflix','Amazon','#californiashutdown','#2020InOneWord',
'#PlayInside','#TigerKingNetflix','#HomeSchoolingIn5Words','#WhenThisIsAllOver','#lovethyneighbor','#TopTenFavoriteFilms',
'#ChurchOnline','#Social_Distancing','#Olympics2020','lockdown','#TacoTuesday','#IKnewIHadCabinFeverWhen','#SomeGoodNews',
'#RentFreeze2020','#OpeningDayAtHome','#InMyAloneTime','#ClapBecauseWeCare','#WhatIAmLearningInQuarantine','#RentRelief',
'#WhenCoronaVirusIsOver','#WhenIRunOutOf','#ImSoBoredI','#NationalDoctorsDay','#workingfromhometips',
'#WaybackInTheGoodOldDays','#TakeOutTuesday','#AprilFoolsDay','carry out','streaming','live sports','Zoom',
'Facetime','mask','hand sanitizer','home workout','Instagram challenge','TikTok',
'NYSE','S&P 500','#marketcrash','NY Fed','USNS Comfort',
'#SuperTuesday2', 'Fauci', 'Trump','Biden','unemployment',
'Seattle','France','Spain','Italy','UK','Michigan','Florida','China','Louisiana','NYC','New York','New Jersey',
'hospital','doctor','nurse','digital date night','essential workers','#handwashingsaveslives','#washyourhands',
'stimulus check','#broke','#startingnewhobbies','#selfcare','procrastination','#quarantinebucketlist','#sweatseveryday',
'bingo']


# Below are loops that query for each trend in the 'trends' array defined above. The query looks for tweets in the range starting 
# Febuary 1, 2020 to April 4, 2020. 300 scraper bots are allocated to get tweets. 
# Uses the query_tweets function from the twitterscraper library 
# Formats the output into dictionary --> one for the trends and the values, and the other for the the tweets and their attributes. Appends each to the correct array. 
# The keys for the trend objects are: 'trend' and 'value'
# The keys for the tweet objects are: 'trend','username','tweet_url','timestamp','text','likes','replies','retweets','img_urls','video_url'

for trend in trends:
    trendDict = {}
    trendDict['trend'] = trend
    count = 0
    for tweet in query_tweets(trend, None, dt.date(2020,2,1), dt.date(2020,4,20),300):
        collection = {}
        collection['trend'] = trend
        collection['username'] = tweet.username
        collection['tweet_url'] = tweet.tweet_url
        collection['timestamp'] = tweet.timestamp
        collection['text'] = tweet.text
        collection['likes'] = tweet.likes
        collection['replies'] = tweet.replies
        collection['retweets'] = tweet.retweets
        collection['img_urls'] = tweet.img_urls
        collection['video_url'] = tweet.video_url
        array.append(collection)
        count = count+1
    trendDict['value'] = count
    trendArray.append(trendDict)

#print(trendArray)
#print(array)
#print(len(array))


# writes the trendArray, which contains the trend dictionaries, to a csv file         
with open('coronaTrends.csv','w',encoding='utf-8', newline='\n') as csvfile:
   writer = csv.DictWriter(csvfile, fieldnames=['trend','value'])
   writer.writeheader()
   writer.writerows(trendArray)
   
 
   
# writes the array, which contains tweet objects in the form of dictionaries, to a csv       
with open('coronaTweets.csv','w', encoding='utf-8', newline='\n') as csvfile:
    fieldnames = ['trend','username','tweet_url','timestamp','text','likes','replies','retweets','img_urls','video_url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(array)
    
#Lets you know that the program is done writing to the csv files     
print('done writing')      



