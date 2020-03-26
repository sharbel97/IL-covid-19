import tweepy
from selenium import webdriver

#initializing twitter access:
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Initiatilizing web driver access and copying the table information:
driver = webdriver.Chrome('/users/sharbel/desktop/twitter-projects/covid-19/chromedriver')
my_url = 'http://www.dph.illinois.gov/topics-services/diseases-and-conditions/diseases-a-z-list/coronavirus'
driver.get(my_url)
container = driver.find_element_by_xpath('//*[@id="content"]/article/div/div/div/dl/dd[1]/div[1]')
table = container.find_elements_by_class_name('NumberHighlight')

#translating HTML into strings in a list
data = []
new_data = []
for post in table:
    data.append(post.text)
driver.close()

#The "tested but negative" element was hidden from main site, 
#but appeared as '' in the list, so this is to handle that:
while ('' in data):
    data.remove('')

#Each list element actually included a new line character,
#This code handles that, by creating a new list.
for i in data:
    new_data.append(i.split('\n'))

positive = new_data[0][1]
deaths = new_data[1][1]
tested = new_data[2][1]

#posting to twitter and handing duplicate post:
try:
    api.update_status('IL COVID-19 Update 🦠🧼‬\n\nPositive🌡 '+ 
                    positive + '\n\nDeaths☠️ '+deaths+ '\n\nTotal tested: '
                    + tested + '\n\n source via DPH website.')
except tweepy.TweepError as error:
    if error.api_code == 187:
        print('Same as previous day results\n\nIL COVID-19 Update 🦠🧼‬\n\nPositive🌡 '+ 
            positive + '\n\nDeaths☠️ '+deaths+ '\n\nTotal tested: '
            + tested + '\n\nsource via DPH website.')

