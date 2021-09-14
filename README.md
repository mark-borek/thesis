Mark Borek Thesis Project: Coronavirus Trends and Tweets

GOALS:
The goals of this project are to collect data from Twitter.com via web scraping techniques using python, provide insights into the data using D3js for visualization, and advance professional ability. 

PURPOSE: 
This project seeks to answer the question of what is important to society today. Given the current pandemic, it is an interesting time to ask what people are spending their time talking about. Twitter is great place to get data that can answer this question, because it has millions of users and billions of tweets. Data visualization using D3js provides a great opportunity to draw out an answer to this question from the data. 

SCOPE: 
This project seeks to provide insight using data collected between February 1, 2020 and April 15, 2020. Therefore, this data provides a survey of the adult American population during this period. 

OBJECTIVES: 
•	Collect and store a large sample size of data from Twitter.com during the above mentioned time period.
•	Create a single-page web application that visualizes the data effortlessly allows the users to interpret the data and draw conclusions to the question asked by the purpose of the project. 
•	Add interactivity to the visualization chart so that the user can interact with the data

DESCRIPTION: 
This project uses a python program to query Twitter.com to tweets based on a string given for the query. It uses the twitterscraper module to do this. The list of strings that are queried for is defined by the developer. The final list includes 142 topics that are related to the Coronavirus Pandemic. These topics include words or phrases that relate the coronavirus to politics, entertainment, sports, location, etc. In total, there are nearly 500,000 tweets collected. 

This project implements a bubble chart as the data visualization. The radius of each of the bubbles that are created for the chart is determined by the number of tweets collected for that topic. Label are given to each of the bubbles, so that the user knows which bubble represents which topic. The user can select any of the topics by clicking or dragging any of the bubbles. Forces are applied to the bubbles so that they are dynamic. Due to the large amount of bubbles, the user is also able to zoom in on the chart. When the user selects a topic from a bubble, the program dynamically loads popular tweets for that topic using the twttr.load module from the Twitter API. Tweets that contain ‘bad words’ are filtered out using a list defined by the developer. When the user selects a new topic, the tweets from the previous topic are removed and the tweets for the new topic are loaded. 

