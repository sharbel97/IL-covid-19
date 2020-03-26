import tweepy
from selenium import webdriver

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

driver = webdriver.Chrome('/users/sharbel/desktop/twitter-projects/covid-19/chromedriver')
my_url = 'http://www.dph.illinois.gov/topics-services/diseases-and-conditions/diseases-a-z-list/coronavirus'
driver.get(my_url)
container = driver.find_element_by_xpath('//*[@id="content"]/article/div/div/div/dl/dd[1]/div[1]')
table = container.find_elements_by_class_name('NumberHighlight')

data = []
new_data = []
for post in table:
    data.append(post.text)
driver.close()

while ('' in data):
    data.remove('')

for i in data:
    new_data.append(i.split('\n'))

positive = new_data[0][1]
deaths = new_data[1][1]
tested = new_data[2][1]
try:
    api.update_status('IL COVID-19 Update 🦠🧼‬\n\nPositive🌡 '+ 
                    positive + '\n\nDeaths☠️ '+deaths+ '\n\nTotal tested: '
                    + tested + '\n\n source via DPH website.')
except tweepy.TweepError as error:
    if error.api_code == 187:
        print('Same as previous day results\n\nIL COVID-19 Update 🦠🧼‬\n\nPositive🌡 '+ 
            positive + '\n\nDeaths☠️ '+deaths+ '\n\nTotal tested: '
            + tested + '\n\nsource via DPH website.')


print('IL COVID-19 Update 🦠🧼‬\n\nPositive🌡 '+ 
                positive + '\n\nDeaths☠️ '+deaths+ '\n\nTotal tested: '
                + tested + '\n\nsource via DPH website.')
